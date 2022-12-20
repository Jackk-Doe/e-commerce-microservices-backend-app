import uuid
from sqlalchemy.orm import Session

import database.models as _models


async def create_inventory(db: Session, p_id: str, amount: int) -> _models.Inventory:
    id = str(uuid.uuid4())
    new_inventory = _models.Inventory(id=id, product_id=p_id, amount=amount)
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory
    