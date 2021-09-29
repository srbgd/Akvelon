from request import Request
import argparse


class ValidationError(Exception):
    pass


class Parser:

    @staticmethod
    def create_validator(args):
        if any(args[i] is None for i in ['first_name', 'last_name', 'email', 'user_id']):
            raise ValidationError("Failed to validate create command")

    @staticmethod
    def read_validator(args):
        if args['user_id'] is None:
            raise ValidationError("Failed to validate read command")

    @staticmethod
    def update_validator(args):
        if args['user_id'] is None and all(args[i] is None for i in ['first_name', 'last_name', 'email']):
            raise ValidationError("Failed to validate update command")

    @staticmethod
    def delete_validator(args):
        if args['user_id'] is None:
            raise ValidationError("Failed to validate delete command")

    @staticmethod
    def init_cli():
        cli = argparse.ArgumentParser(description='Console gRPC client to Flask application.')
        parsers = cli.add_subparsers(help='Available commands')

        user_parser = parsers.add_parser('user', help='User management command')
        user_parser.add_argument('crud_action', choices=['create', 'read', 'update', 'delete'])
        user_parser.add_argument('--first_name')
        user_parser.add_argument('--last_name')
        user_parser.add_argument('--email')
        user_parser.add_argument('--user_id')

        return cli

    def __init__(self):
        self.cli = self.init_cli()

        self.validators = {
            'create': self.create_validator,
            'read': self.read_validator,
            'update': self.update_validator,
            'delete': self.delete_validator,
        }

    def parse(self, args):
        namespace = self.cli.parse_args(args)

        data = vars(namespace)
        method = data.pop('crud_action')

        self.validators[method](data)

        return Request(method, data)
