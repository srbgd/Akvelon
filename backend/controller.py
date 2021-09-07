"""
Module which defines endpoint controllers
"""

from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from . import schema
from . import handler


class BaseController:
    """
    Base controller for any endpoint.

    Validates request with schema and dispatches it to the correct handler
    """

    schemas: dict
    handlers: dict

    def validate(self, request):
        """
        Validate json schema of incoming request.

        :param request: flask.Request instance
        :return: result of schema serialization and request's method
        """

        method = request.method
        if method not in self.schemas:
            ValidationError(f'No schema for method {method}')

        try:
            body = request.get_json()
        except BadRequest:
            raise ValidationError('Incorrect json data')

        if body is None:
            raise ValidationError('Body cannot be empty')

        result = self.schemas[method].load(data=body)

        return result, method

    def handle(self, request):
        """
        Handles request by dispatching it to the correct handler based on request's method
        :param request: flask.Request instance
        :return: result of request handling
        """

        data, method = self.validate(request)
        return self.handlers[method](data)


class UserController(BaseController):
    """
    User endpoint controller
    """

    schemas = {
        'POST': schema.UserPostSchema(),
        'GET': schema.UserGetSchema(),
        'PATCH': schema.UserPatchSchema(),
        'DELETE': schema.UserDeleteSchema(),
    }

    handlers = {
        'POST': handler.create_user,
        'GET': handler.read_user,
        'PATCH': handler.update_user,
        'DELETE': handler.delete_user,
    }


class TransactionController(BaseController):
    """
    Transaction endpoint controller
    """

    schemas = {
        'POST': schema.TransactionPostSchema(),
        'GET': schema.TransactionGetSchema(),
        'PATCH': schema.TransactionPatchSchema(),
        'DELETE': schema.TransactionDeleteSchema(),
    }

    handlers = {
        'POST': handler.create_transaction,
        'GET': handler.read_transaction,
        'PATCH': handler.update_transaction,
        'DELETE': handler.delete_transaction,
    }


class QueryController(BaseController):
    """
    Query endpoint controller
    """

    schemas = {
        'GET': schema.QueryGetSchema(),
    }

    handlers = {
        'GET': handler.serve_query,
    }


class ResetController(BaseController):
    """
    Reset endpoint controller (testing only)
    """

    schemas = {
        'DELETE': schema.ResetDeleteSchema(),
    }

    handlers = {
        'DELETE': handler.reset_db,
    }


class FibonacciController(BaseController):
    """
    Fibonacci endpoint controller (testing only)
    """

    schemas = {
        'GET': schema.FibonacciGetSchema(),
    }

    handlers = {
        'GET': handler.get_fibonacci_number,
    }
