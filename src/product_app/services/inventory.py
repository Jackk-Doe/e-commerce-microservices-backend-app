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
    

async def get_inventory_by_product_id(db: Session, p_id: str) -> _models.Inventory:
    return db.query(_models.Inventory).filter(_models.Inventory.product_id==p_id).first()


async def delete_inventory_by_product_id(db: Session, p_id: str) -> None:
    inventory = await get_inventory_by_product_id(db=db, p_id=p_id)
    if not inventory:
        # If no Inventory, stop here
        return
    db.delete(inventory)
    db.commit()


async def update_inventory(db: Session, p_id: str, amount: int) -> _models.Inventory:
    inventory = await get_inventory_by_product_id(db=db, p_id=p_id)
    if not inventory:
        # If no Inventory obj of the updating Product, create new
        inventory = await create_inventory(db=db, p_id=p_id, amount=amount)
    else:
        inventory.amount = amount
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
    return inventory