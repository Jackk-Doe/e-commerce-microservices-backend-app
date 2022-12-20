import uuid
from sqlalchemy.orm import Session

import database.models as _models


async def create_product(db: Session, name: str, des: str, price: float, seller_id: str) -> _models.Product:
    id = str(uuid.uuid4())
    # TODO : put codes below in try-catch
    product = _models.Product(
        id=id, name=name, description=des, price=price, seller_id=seller_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


async def get_products(db: Session) -> list[_models.Product]:
    return db.query(_models.Product).all()


async def get_product_by_id(db: Session, id: str) -> _models.Product:
    return db.query(_models.Product).get(id)


async def delete_product(db: Session, product_id: str):
    product = await get_product_by_id(db=db, id=product_id)
    db.delete(product)
    db.commit()