import grpc

import envs as _envs
import user_pb2 as _pb_user
from user_pb2_grpc import UserStub

'''
CLIENT ACCESSIBLE Services
'''


'''
MICROSERVICES INTERNAL ONLY Services
'''
async def internal_get_user_via_token(token: str) -> _pb_user.InternalUserDTO:
    async with grpc.aio.insecure_channel(_envs.USER_URL) as channel:
        stub = UserStub(channel=channel)
        user = await stub.InternalGetUserViaToken(_pb_user.Token(value=token))
    return user


async def internal_get_user_via_id(u_id: str) -> _pb_user.InternalUserDTO:
    async with grpc.aio.insecure_channel(_envs.USER_URL) as channel:
        stub = UserStub(channel=channel)
        user = await stub.InternalGetUserViaId(_pb_user.Id(value=u_id))
    return user