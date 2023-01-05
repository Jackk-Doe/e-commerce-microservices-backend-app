import passlib.hash as _hash
from sqlalchemy import Column, String

from . import db as _db
from user_pb2 import UserDTO, InternalUserDTO, UserDTOWithToken

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
    def toUserDTO(self) -> UserDTO:
        return UserDTO(
            name=self.name,
            email=self.email
        )

    # Convert User model to gRPC UserDTOWithToken
    def toUserDTOWithToken(self, token: str) -> UserDTOWithToken:
        return UserDTOWithToken(
            name=self.name,
            email=self.email,
            token=token
        )

    # Convert User model to gRPC InternalUserDTO
    def toInternalUserDTO(self) -> InternalUserDTO:
        return InternalUserDTO(
            name=self.name,
            email=self.email,
            id=self.id
        )


# Connect or Initialize database
def connect_or_initialize_db():
    _db.Base.metadata.create_all(bind=_db.engine)