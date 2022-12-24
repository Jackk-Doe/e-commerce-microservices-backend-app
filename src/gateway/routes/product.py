import http
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from grpc.aio import AioRpcError

import schemas.product as _schema_product
import grpc_services.product as _grpc_serv_product
import grpc_services.user as _grpc_serv_user
import utils.grpc_status_code as _util_grpc_status_code


# Access token via this variable
# NOTE: if token is not given, when using this var, throw error
_token_auth_scheme = OAuth2PasswordBearer(tokenUrl='api/user/token' ,auto_error=False)

# Create Product APIrouter
router = APIRouter(prefix="/product")


@router.get('/test')
async def testRoute():
    return {"Test": "Product route"}


@router.get('/{p_id}')
async def get_product_by_id(p_id: str):
    try:
        product = await _grpc_serv_product.get_product_by_id(p_id=p_id)
    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return _schema_product.from_product_grpc_message(product=product)


@router.get('/')
async def get_products():
    try:
        products = await _grpc_serv_product.get_products()
    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return [_schema_product.from_product_grpc_message(product=product) for product in products]


@router.post('/')
async def create_product(
    body_input: _schema_product.ProductInputForm, 
    token: str = Depends(_token_auth_scheme)
):
    if token is None:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Token is required')

    try:
        # Get User data
        user = await _grpc_serv_user.internal_get_user_via_token(token=token)
        
        # Create Product
        product = await _grpc_serv_product.create_product(
            u_id=user.id,
            name=body_input.name,
            des=body_input.description,
            price=body_input.price,
            amount=body_input.amount
        )

    except AioRpcError as rpc_err:
        http_status = await _util_grpc_status_code.convert_to_http_status_code(rpc_err.code())
        raise HTTPException(status_code=http_status, detail=rpc_err.details())
    except Exception as err:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(err))

    return _schema_product.from_product_grpc_message(product=product)