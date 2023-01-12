import grpc

import envs as _envs
import product_pb2 as _pb_product
from product_pb2_grpc import ProductStub


async def get_product_by_id(p_id: str) -> _pb_product.ProductDTO:
    async with grpc.aio.insecure_channel(_envs.PRODUCT_URL) as channel:
        stub = ProductStub(channel=channel)
        product = await stub.GetProductById(_pb_product.Id(value=p_id))
    return product


async def get_products(page: int, limit: int) -> list[_pb_product.ProductListDTO]:
    async with grpc.aio.insecure_channel(_envs.PRODUCT_URL) as channel:
        stub = ProductStub(channel=channel)

        # products_input = _pb_product.ProductListInput(page=page, limit=limit)
        products_dto = await stub.GetProducts(_pb_product.ProductListInput(page=page, limit=limit))
    return products_dto

    #     products = []
    #     async for product in stub.GetProducts(_pb_product.Null()):
    #         products.append(product)

    # return products


async def create_product(u_id: str, name: str, des: str, price: float, amount: int) -> _pb_product.ProductDTO:
    async with grpc.aio.insecure_channel(_envs.PRODUCT_URL) as channel:
        stub = ProductStub(channel=channel)
        product = await stub.CreateProduct(_pb_product.ProductInputForm(
            name=name,
            description=des,
            seller_id=u_id,
            price=price,
            amount=amount
        ))
    return product