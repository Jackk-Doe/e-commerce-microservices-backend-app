from pydantic import BaseModel

import user_pb2 as _pb_user


class UserDTO(BaseModel):
    name: str
    email: str


class UserSignUpForm(BaseModel):
    name: str
    email: str
    password: str


# Create UserDTO schema, from arg of user grpc message
def from_user_grpc_message(user: _pb_user) -> UserDTO:
    return UserDTO(
        name=user.name,
        email=user.email
    )