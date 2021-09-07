"""
Module which redefines basic Marshmallow for better error handling
"""

from flask_marshmallow import base_fields


class Integer(base_fields.Integer):

    default_error_messages = {'invalid': 'Not a valid integer.'}


class UUID(base_fields.UUID):

    default_error_messages = {'invalid_uuid': 'Not a valid UUID.'}


class Email(base_fields.Email):

    default_error_messages = {'invalid': 'Not a valid email address.'}


class NonBlankString(base_fields.String):

    default_error_messages = {
        'blank': 'Field cannot be blank.',
        'invalid': 'Not a valid string.'
    }

    def _validate(self, value):
        value = (value if value is not None else '').strip()
        super()._validate(value)
        if value == '':
            self.fail('blank')


class Date(base_fields.Date):

    default_error_messages = {'invalid': 'Not a valid date.'}
