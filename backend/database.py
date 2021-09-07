"""
Module defining SQLAlchemy ORM models
"""

from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID, DATE
from . import db
import uuid


class User(db.Model):
    """
    Model for storing user entity in DB
    """

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    is_deleted = Column(Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'(id={self.id},' \
               f'first_name={self.first_name},' \
               f'last_name={self.last_name},' \
               f'email={self.email},' \
               f'is_deleted={self.is_deleted})'


class Transaction(db.Model):
    """
    Model for storing transaction entity in DB
    """

    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(DATE, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'(id={self.id},' \
               f'date={self.date},' \
               f'amount={self.amount},' \
               f'user_id={self.user_id},' \
               f'is_deleted={self.is_deleted})'
