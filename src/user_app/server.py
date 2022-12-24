import grpc
import logging

import envs as _envs
import database.db as _db
import services.user as _services_user
from user_pb2 import Id, Token, UserSignUpForm, UserLogInForm, UserDTO
from user_pb2_grpc import UserServicer, add_UserServicer_to_server


# My logging config
logger = logging.getLogger(__name__)

# Return database local Session, use this returning Session to interact with db
def get_db_session():
    return _db.SessionLocal()


class User(UserServicer):

    '''

    CLIENT ACCESSIBLE Services
    
    '''

    async def LogIn(self, request, context):
        with get_db_session() as db_session:
            try:
                existed_user = await _services_user.get_user_by_email(db=db_session, email=request.email)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            # Check input name and email already existed
            if existed_user is None:
                await context.abort(grpc.StatusCode.NOT_FOUND, 'User with the given name or email is NOT existed')

            # Check Password matching
            if existed_user.verify_password(password=request.password) == False:
                await context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Input password is not matched')

            token = await _services_user.generate_token(u_id=existed_user.id)
            user_dto = existed_user.toUserDTO(token=token)

        return user_dto


    async def SignUp(self, request, context):
        with get_db_session() as db_session:
            try:
                existed_user = await _services_user.get_user_by_name_or_email(db=db_session, name=request.name, email=request.email)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            # Check input name and email already existed
            if existed_user:
                await context.abort(grpc.StatusCode.ALREADY_EXISTS, 'User with the given name or email is ALREADY existed')

            try:
                # Create new User, and save to database
                new_user = await _services_user.sign_up_user(db=db_session, name=request.name, email=request.email, password=request.password)

            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            token = await _services_user.generate_token(u_id=new_user.id)
            user_dto = new_user.toUserDTO(token=token)

        return user_dto


    async def GetMe(self, request, context):
        with get_db_session() as db_session:
            try:
                user = await _services_user.get_user_by_token(db=db_session, token=request.value)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            if user is None:
                await context.abort(grpc.StatusCode.NOT_FOUND, 'User from a decoded input token is not found')

            user_dto = user.toUserDTO(token=request.value)

        return user_dto


    '''

    MICROSERVICES INTERNAL ONLY Services

    '''

    async def GetId(self, request, context):
        with get_db_session() as db_session:
            try:
                user = await _services_user.get_user_by_token(db=db_session, token=request.value)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            if user is None:
                await context.abort(grpc.StatusCode.NOT_FOUND, 'User of a input Id is not found')

            id = Id(value=user.id)
        # Return User.id from input token
        return id


    async def InternalGetMe(self, request, context):
        with get_db_session() as db_session:
            try:
                user = await _services_user.get_user_by_token(db=db_session, token=request.value)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))

            if user is None:
                await context.abort(grpc.StatusCode.NOT_FOUND, 'User from a decoded input token is not found')

            user_dto = user.toInternalUserDTO(token=request.value)

        return user_dto


# Function to run Server
async def run_server():
    PORT = _envs.PORT

    # Server set up
    server = grpc.aio.server()
    add_UserServicer_to_server(User(), server=server)
    server.add_insecure_port(f"[::]:{PORT}")

    # Start running
    await server.start()
    logging.info("User gRPC Asynchronous-Server is up and running...")

    await server.wait_for_termination()