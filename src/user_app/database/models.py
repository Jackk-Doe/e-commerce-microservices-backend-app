from sqlalchemy import Column, String

from . import db as _db
from user_pb2 import UserDTO

class User(_db.Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<User name({self.name}); email({self.email}); id({self.id})>"

    def toUserDTO(self, token: str) -> UserDTO:
        return UserDTO(
            name=self.name,
            email=self.email,
            token=token
        )


# Connect or Initialize database
def connect_or_initialize_db():
    _db.Base.metadata.create_all(bind=_db.engine)