from pydantic import BaseModel


class ProductDTO(BaseModel):
    id: str
    name: str
    description: str
    seller_id: str
    image_path: str
    price: float
    amount: int