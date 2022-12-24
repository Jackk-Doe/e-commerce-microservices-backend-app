from pydantic import BaseModel

import product_pb2 as _pb_product


class ProductDTO(BaseModel):
    id: str
    name: str
    description: str
    seller_id: str
    image_path: str
    price: float
    amount: int


# Create ProductDTO schema, from arg of product grpc message
def from_product_grpc_message(product: _pb_product.ProductDTO) -> ProductDTO:
    return ProductDTO(
        id=product.id,
        name=product.name,
        description=product.description,
        seller_id=product.seller_id,
        image_path=product.image_path,
        price=product.price,
        amount=product.amount,
    )