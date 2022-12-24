import http
from fastapi import APIRouter, HTTPException
from grpc.aio import AioRpcError

import schemas.product as _schema_product
import grpc_services.product as _grpc_serv_product
import utils.grpc_status_code as _util_grpc_status_code

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