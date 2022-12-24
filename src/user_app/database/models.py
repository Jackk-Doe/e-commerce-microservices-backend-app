import passlib.hash as _hash
from sqlalchemy import Column, String

from . import db as _db
from user_pb2 import UserDTO, InternalUserDTO

class User(_db.Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<User name({self.name}); email({self.email}); id({self.id})>"

    # Verify User hashed [password] with arg password, return Boolean
    def verify_password(self, password: str) -> bool:
        return _hash.bcrypt.verify(password, self.password)

    # Convert User model to gRPC UserDTO
    def toUserDTO(self, token: str) -> UserDTO:
        return UserDTO(
            name=self.name,
            email=self.email,
            token=token
        )

    # Convert User model to gRPC InternalUserDTO
    def toInternalUserDTO(self, token: str) -> InternalUserDTO:
        return InternalUserDTO(
            name=self.name,
            email=self.email,
            token=token,
            id=self.id
        )


# Connect or Initialize database
def connect_or_initialize_db():
    _db.Base.metadata.create_all(bind=_db.engine)