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

    async def LogIn(self, request, context):
        # TODO : Implement logic
        return super().LogIn(request, context)


    async def SignUp(self, request, context):
        with get_db_session() as db_session:
            # TODO : Check User.name & User.email already existed
            try:
                new_user = await _services_user.sign_up_user(db=db_session, name=request.name, email=request.email, password=request.password)
            except Exception as err:
                await context.abort(grpc.StatusCode.INTERNAL, str(err))
            # TODO : Generate JWT
            user_dto = new_user.toUserDTO(token="This_is_token")
        return user_dto


    async def GetMe(self, request, context):
        # TODO : Implement logic
        return super().GetMe(request, context)


    async def GetId(self, request, context):
        # TODO : Implement logic
        return super().GetId(request, context)


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