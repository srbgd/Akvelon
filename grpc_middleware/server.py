import asyncio

import grpc
from user_pb2 import CreateReply, ReadReply, UpdateReply
from user_pb2_grpc import UserServicer, add_UserServicer_to_server


class UserService(UserServicer):

    async def Create(self, request, context):
        print(request)
        return CreateReply(
            user_id=request.user_id,
        )

    async def Read(self, request, context):
        print(request)
        return ReadReply(
            user_id=request.user_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
        )

    async def Update(self, request, context):
        print(request)
        return UpdateReply(
            user_id=request.user_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
        )

    async def Delete(self, request, context):
        print(request)
        return None


async def serve() -> None:
    server = grpc.aio.server()
    add_UserServicer_to_server(UserService(), server)
    listen_address = '[::]:50051'
    server.add_insecure_port(listen_address)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
