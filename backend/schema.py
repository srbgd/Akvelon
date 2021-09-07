"""
Module defining schemas for requests validation and serialization
"""

from marshmallow import validates_schema, ValidationError, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from . import ma
from backend import fields
from .database import User, Transaction

__all__ = [
    'UserPostSchema',
    'UserGetSchema',
    'UserPatchSchema',
    'UserDeleteSchema',
    'UserSchema',
    'TransactionPostSchema',
    'TransactionGetSchema',
    'TransactionPatchSchema',
    'TransactionDeleteSchema',
    'TransactionSchema',
    'QueryGetSchema',
    'ResetDeleteSchema',
    'FibonacciGetSchema',
]


class BasePatchSchemaValidator(ma.Schema):
    """
    A schema which validates that PATCH request has at least one optional param to be updated
    """

    _optional_fields: tuple

    @validates_schema
    def validate_optional_fields(self, data, **kwargs):
        if all(field not in data for field in self._optional_fields):
            raise ValidationError("Any optional field should present")


class UserPostSchema(ma.Schema):
    """
    User creation schema
    """

    first_name = fields.NonBlankString(required=True)
    last_name = fields.NonBlankString(required=True)
    email = fields.Email(required=True)


class UserGetSchema(ma.Schema):
    """
    User reading schema
    """

    id = fields.UUID(required=True)


class UserPatchSchema(BasePatchSchemaValidator):
    """
    User updating schema
    """

    id = fields.UUID(required=True)
    first_name = fields.NonBlankString(required=False)
    last_name = fields.NonBlankString(required=False)
    email = fields.Email(required=False)

    _optional_fields = ('first_name', 'last_name', 'email')


class UserDeleteSchema(ma.Schema):
    """
    User deletion schema
    """

    id = fields.UUID(required=True)


class UserSchema(SQLAlchemyAutoSchema):
    """
    Schema for storing user entities in postgres DB
    """

    class Meta:
        model = User


class TransactionPostSchema(ma.Schema):
    """
    Transaction creation schema
    """

    user_id = fields.UUID(required=True)
    amount = fields.Integer(required=True)
    date = fields.Date(required=True)


class TransactionGetSchema(ma.Schema):
    """
    Transaction reading schema
    """

    id = fields.UUID(required=True)


class TransactionPatchSchema(BasePatchSchemaValidator):
    """
    Transaction updating schema
    """

    id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    amount = fields.Integer(required=True)
    date = fields.Date(required=True)

    _optional_fields = ('user_id', 'amount', 'date')


class TransactionDeleteSchema(ma.Schema):
    """
    Transaction deletion schema
    """

    id = fields.UUID(required=True)


class TransactionSchema(SQLAlchemyAutoSchema):
    """
    Schema for storing transaction entities in postgres DB
    """

    class Meta:
        model = Transaction
        include_relationships = True


class QueryGetSchema(ma.Schema):
    """
    Information querying schema
    """

    user_id = fields.UUID(required=False)
    date = fields.Date(required=False)
    type = fields.NonBlankString(validate=validate.OneOf(['income', 'outcome']), required=False)


class ResetDeleteSchema(ma.Schema):
    """
    DB resetting schema
    """

    confirmation = fields.NonBlankString(validate=validate.Equal('secret_value_441e'), required=True)
    table = fields.NonBlankString(validate=validate.OneOf(['users', 'transactions']), required=False)


class FibonacciGetSchema(ma.Schema):
    """
    N-th Fibonacci number computing schema
    """

    number = fields.Integer(validate=validate.Range(min=0, max=1000000), required=True)
