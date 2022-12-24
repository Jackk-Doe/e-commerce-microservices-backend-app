import grpc

import envs as _envs
import product_pb2 as _pb_product
from product_pb2_grpc import ProductStub


async def get_product_by_id(p_id: str) -> _pb_product.ProductDTO:
    async with grpc.aio.insecure_channel(_envs.PRODUCT_URL) as channel:
        stub = ProductStub(channel=channel)
        product = await stub.GetProductById(_pb_product.Id(value=p_id))
    return product