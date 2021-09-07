"""
Main module of the application used to create flask instance and define endpoints
"""

from . import get_flask_app
from flask import request
from .controller import (
    UserController,
    TransactionController,
    QueryController,
    ResetController,
    FibonacciController,
)


# Endpoint controllers
user_controller = UserController()
transaction_controller = TransactionController()
query_controller = QueryController()
reset_controller = ResetController()
fibonacci_controller = FibonacciController()

flask_app = get_flask_app()


@flask_app.route("/user", methods=['POST', 'GET', 'PATCH', 'DELETE'])
def manage_users():
    """
    CRUD endpoint for user management
    :return: HTTP status and json representation of a user when needed
    """
    return user_controller.handle(request)


@flask_app.route("/transaction", methods=['POST', 'GET', 'PATCH', 'DELETE'])
def manage_transactions():
    """
    CRUD endpoint for transaction management
    :return: HTTP status and json representation of a transaction when needed
    """
    return transaction_controller.handle(request)


@flask_app.route("/query", methods=['GET'])
def information_querying():
    """
    Endpoint for information querying
    :return: Json with a list of queried transactions and a sum of transactions' amounts
    """
    return query_controller.handle(request)


@flask_app.route("/reset", methods=['DELETE'])
def reset():
    """
    Endpoint for DB clearing (testing only)
    :return: Status code 200 if request was handled correctly
    """
    return reset_controller.handle(request)


@flask_app.route("/fibonacci", methods=['GET'])
def fibonacci():
    """
    Endpoint for getting n-th fibonacci number (testing only)
    :return: Json with n-th fibonacci number
    """
    return fibonacci_controller.handle(request)
