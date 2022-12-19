from sqlalchemy import Column, String, Float

from . import db as _db
from product_pb2 import ProductDTO

class Product(_db.Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    seller_id = Column(String, nullable=False)
    image_url = Column(String)

    # TODO : Update thie method later
    def __repr__(self) -> str:
        return f"Product name({self.name}) des({self.description})"

    # Convernt Product model to gRPC message ProductDTO
    def toProductDTO(self, amount: int) -> ProductDTO:
        return ProductDTO(
            name=self.name,
            description=self.description,
            seller_id=self.seller_id,
            price=self.price,
            id=self.id,
            image_path=self.image_url,
            amount=amount,
        )


# Connect or Initialize database
def connect_or_initialize_db():
    _db.Base.metadata.create_all(bind=_db.engine)