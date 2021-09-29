import asyncio

import grpc
from user_pb2 import CreateRequest, ReadRequest, UpdateRequest, DeleteRequest
from user_pb2_grpc import UserStub


class UserGrpcService:

    def __init__(self, address):
        self.address = address
        self.handlers = {
            'create': self.create,
            'read': self.read,
            'update': self.update,
            'delete': self.delete,
        }

    async def create(self, data):
        print(data)
        async with grpc.aio.insecure_channel(self.address) as channel:
            return await UserStub(channel).Create(CreateRequest(**data))

    async def read(self, data):
        async with grpc.aio.insecure_channel(self.address) as channel:
            return await UserStub(channel).Read(ReadRequest(**data))

    async def update(self, data):
        async with grpc.aio.insecure_channel(self.address) as channel:
            return await UserStub(channel).Update(UpdateRequest(**data))

    async def delete(self, data):
        async with grpc.aio.insecure_channel(self.address) as channel:
            return await UserStub(channel).Delete(DeleteRequest(**data))

    def send(self, request):
        return asyncio.run(self.handlers[request.method](request.data))
