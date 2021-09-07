"""
Module with request handlers

Handlers receive request's json and return HTTP status code and response's json when needed
"""

from .database import User, Transaction
from http.client import OK
from flask import abort, Response
from . import db
from .schema import UserSchema, TransactionSchema
from sqlalchemy import or_
from .utils import fibonacci


# marshmallow_sqlalchemy schemas for storing entities in postgres DB
user_schema = UserSchema()
transaction_schema = TransactionSchema()

# dict to map reset table param to the list of models to be reset
models = {
    None: [User, Transaction],
    'users': [User],
    'transactions': [Transaction]
}


def get_user(user_id: str):
    """
    Not a handler. Just helping function to get a user or raise a NotFound exception

    :param user_id: uuid of requested user
    :return: json with user's data
    """

    result = db.session.query(User).get(user_id)
    if result is None or result.is_deleted:
        abort(404, description=f'User with id {user_id} not found')
    return result


def create_user(data: dict):
    """
    Handle create user request

    :param data: json with user's data
    :return: json with data of created user
    """

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    result = user_schema.dump(new_user)
    return result, OK


def read_user(data: dict):
    """
    Handle read user request

    :param data: json with user id to be read
    :return: json with read user
    """

    return user_schema.dump(get_user(data['id'])), OK


def update_user(data: dict):
    """
    Handle update user request

    :param data: json with params to be updated
    :return: json with updated user
    """

    user = get_user(data.pop('id'))
    for k, v in data.items():
        setattr(user, k, v)
    db.session.commit()
    return user_schema.dump(user), OK


def delete_user(data: dict):
    """
    Handle delete user request

    :param data: json with user id to be deleted
    :return: HTTP status code 200 if user was deleted successfully
    """

    user = get_user(data['id'])
    user.is_deleted = True
    db.session.commit()
    return Response(status=200)


def get_transaction(transaction_id: str):
    """
    Not a handler. Just helping function to get a transaction or raise a NotFound exception

    :param transaction_id: uuid of requested transaction
    :return: json with transaction's data
    """

    result = db.session.query(Transaction).get(transaction_id)
    if result is None or result.is_deleted:
        abort(404, description=f'Transaction with id {transaction_id} not found')
    return result


def create_transaction(data: dict):
    """
    Handle create transaction request

    :param data: json with transaction's data
    :return: json with data of created transaction
    """

    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    result = transaction_schema.dump(new_transaction)
    return result, OK


def read_transaction(data: dict):
    """
    Handle read transaction request

    :param data: json with transaction id to be read
    :return: json with read transaction
    """

    return transaction_schema.dump(get_transaction(data['id'])), OK


def update_transaction(data: dict):
    """
    Handle update transaction request

    :param data: json with params to be updated
    :return: json with updated transaction
    """

    transaction = get_transaction(data.pop('id'))
    for k, v in data.items():
        setattr(transaction, k, v)
    db.session.commit()
    return transaction_schema.dump(transaction), OK


def delete_transaction(data: dict):
    """
    Handle delete transaction request

    :param data: json with transaction id to be deleted
    :return: HTTP status code 200 if transaction was deleted successfully
    """

    transaction = get_transaction(data['id'])
    transaction.is_deleted = True
    db.session.commit()
    return Response(status=200)


def serve_query(data: dict):
    """
    Handle information querying request

    :param data: params of a query
    :return: json with a list of queried transactions and a sum of transactions' amounts
    """
    if data == dict():
        # Select all transaction i DB
        result = db.session.query(Transaction).filter(Transaction.is_deleted == False)
    else:
        result = db.session.query(Transaction).filter(or_(
            # Select transaction with specific user_id
            Transaction.user_id == data.get('user_id'),
            # Select transaction with specific date
            Transaction.date == data.get('date'),
            # Select transaction with positive or negative amount
            Transaction.amount > 0 if data.get('type') == 'income' else False,
            Transaction.amount < 0 if data.get('type') == 'outcome' else False
            )
        )
    transactions = [transaction_schema.dump(transaction) for transaction in result.all()]
    transactions_sum = sum([transaction['amount'] for transaction in transactions])
    return {'transactions': transactions, 'sum': transactions_sum}, OK


def reset_db(data: dict):
    """
    Handle DB reset request

    :param data: json with tables to be deleted
    :return: HTTP status code 200 if table was deleted successfully
    """

    for model in models[data.get('table')]:
        db.session.query(model).delete()
    db.session.commit()
    return Response(status=200)


def get_fibonacci_number(data: dict):
    """
    Handle get n'th fibonacci number request

    :param data: json with a sequential number to be computed
    :return: json with n-th fibonacci number
    """

    return {'answer': fibonacci(data['number'])}, OK
