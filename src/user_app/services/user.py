import uuid
from sqlalchemy import or_
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from jwt import encode as jwt_encode
from jwt import decode as jwt_decode

import envs as _envs
import database.models as _models


async def sign_up_user(db: Session, name: str, email: str, password: str) -> _models.User:
    id = str(uuid.uuid4())
    hashed_password = bcrypt.hash(password)
    new_user = _models.User(
        id=id, name=name, email=email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Create a Token base on User.id
async def generate_token(u_id: str) -> str:
    return jwt_encode(payload={"id": u_id}, key=_envs.JWT_SERCRET)
    

# Find a User where, matched param.name or param.email, or return None
async def get_user_by_name_or_email(db: Session, name: str, email: str) -> _models.User:
    return db.query(_models.User).filter(or_(_models.User.name == name, _models.User.email == email)).first()