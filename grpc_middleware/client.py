from parser import Parser, ValidationError
from grpc_service import UserGrpcService
import sys

parser = Parser()
user_grpc_service = UserGrpcService('localhost:50051')


def main():
    try:
        request = parser.parse(sys.argv[1:])
    except ValidationError as err:
        print(err)
    else:
        print(user_grpc_service.send(request))


if __name__ == '__main__':
    main()
