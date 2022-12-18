from sqlalchemy import Column, String, Float

from . import db as _db

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


# Connect or Initialize database
def connect_or_initialize_db():
    _db.Base.metadata.create_all(bind=_db.engine)