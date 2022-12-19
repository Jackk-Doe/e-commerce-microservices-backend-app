import uuid
from sqlalchemy.orm import Session

import database.models as _db_pd


async def create_product(db: Session, name: str, des: str, price: float, seller_id: str) -> _db_pd.Product:
    id = str(uuid.uuid4())
    # TODO : put codes below in try-catch
    product = _db_pd.Product(
        id=id, name=name, description=des, price=price, seller_id=seller_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
