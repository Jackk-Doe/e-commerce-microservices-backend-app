import http
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from grpc.aio import AioRpcError

import schemas.user as _schema_user
import grpc_services.user as _grpc_serv_user
import utils.grpc_status_code as _util_grpc_status_code


# Access token via this variable
# NOTE: if token is not given, when using this var, throw error
_token_auth_scheme = OAuth2PasswordBearer(tokenUrl='api/user/token' ,auto_error=False)


router = APIRouter(prefix="/user")


@router.get('/test')
async def testRoute():
    return {"Test": "User router"}


@router.get('/me')
async def get_me(token: str = Depends(_token_auth_scheme)):
    if token is None:
        raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail='Token is required')
    
    try:
        user = await _grpc_serv_user.internal_get_user_via_token(token=token)

    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return _schema_user.from_user_grpc_message(user=user)


@router.post('/signup')
async def signup_user(form_data: _schema_user.UserSignUpForm):
    try:
        new_user = await _grpc_serv_user.sign_up_user(
            name=form_data.name,
            email=form_data.email,
            password=form_data.password
        )
    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return _schema_user.from_user_grpc_message_with_token(user=new_user)


@router.post('/login')
async def login_user(form_data: _schema_user.UserLogInForm):
    try:
        user = await _grpc_serv_user.log_in_user(
            email=form_data.email,
            password=form_data.password
        )
    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return _schema_user.from_user_grpc_message_with_token(user=user)
