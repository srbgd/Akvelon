import requests
from os import environ
from utils import get_json


class API:

    def __init__(self, url=environ.get('FLASK_APP_URL', 'http://127.0.0.1:80')):
        self.url = url

    @get_json()
    def post_user(self, first_name: str, last_name: str, email: str):
        return requests.post(f'{self.url}/user', json={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        })

    @get_json()
    def get_user(self, uuid: str):
        return requests.get(f'{self.url}/user', json={'id': uuid})

    @get_json()
    def patch_user(self, uuid: str, first_name=None, last_name=None, email=None):
        return requests.patch(f'{self.url}/user', json={
            k: v for k, v in {
                'id': uuid,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
            }.items() if v not in (None, '')
        })

    @get_json()
    def delete_user(self, uuid: str):
        return requests.delete(f'{self.url}/user', json={'id': uuid})

    @get_json()
    def post_transaction(self, user_id: str, amount: int, date: str):
        return requests.post(f'{self.url}/transaction', json={
            'user_id': user_id,
            'amount': amount,
            'date': date,
        })

    @get_json()
    def get_transaction(self, uuid: str):
        return requests.get(f'{self.url}/transaction', json={'id': uuid})

    @get_json()
    def patch_transaction(self, uuid: str, user_id=None, amount=None, date=None):
        return requests.patch(f'{self.url}/transaction', json={
            k: v for k, v in {
                'id': uuid,
                'user_id': user_id,
                'amount': amount,
                'date': date,
            }.items() if v not in (None, '')
        })

    @get_json()
    def delete_transaction(self, uuid: str):
        return requests.delete(f'{self.url}/transaction', json={'id': uuid})

    @get_json()
    def query(self, user=None, date=None, type=None):
        return requests.get(f'{self.url}/query', json={
            k: v for k, v in {
                'user_id': user,
                'date': date,
                'type': type,
            }.items() if v not in (None, '')
        })

    @get_json(decorator_return_value=False)
    def reset(self, table=None):
        return requests.delete(f'{self.url}/reset', json={
            k: v for k, v in {
                'confirmation': 'secret_value_441e',
                'table': table,
            }.items() if v not in (None, '')
        })

    @get_json()
    def get_fibonacci(self, number: int):
        return requests.get(f'{self.url}/fibonacci', json={'number': number})
