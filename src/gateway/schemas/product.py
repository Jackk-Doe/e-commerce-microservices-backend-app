from pydantic import BaseModel

import product_pb2 as _pb_product


class ProductDTO(BaseModel):
    id: str
    name: str
    description: str
    seller_name: str
    image_path: str
    price: float
    amount: int


class ProductInputForm(BaseModel):
    name: str
    description: str
    price: float
    amount: int
    # TODO: Add image upload later


# Create ProductDTO schema, from arg of product grpc message
def from_product_grpc_message(product: _pb_product.ProductDTO, u_name: str) -> ProductDTO:
    return ProductDTO(
        id=product.id,
        name=product.name,
        description=product.description,
        seller_name=u_name,
        image_path=product.image_path,
        price=product.price,
        amount=product.amount,
    )