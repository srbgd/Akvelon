from client import API
from pytest import fixture
from utils import post_user, get_ids


class TestQueries:

    api = API()

    def post_user(self, number: int):
        return post_user(self.api, 'query', number)

    @fixture(autouse=True)
    def set_up(self):
        self.api.reset()
        self.user_id_1, self.user_id_2 = self.post_user(1)['id'], self.post_user(2)['id']
        self.api.get_user(self.user_id_1)
        self.api.get_user(self.user_id_2)
        self.date_1, self.date_2 = '2021-05-11', '2021-05-12'
        users_id = [self.user_id_1] * 3 + [self.user_id_2] * 2
        amounts = [10, 20, -30, 40, 50]
        dates = [self.date_1, self.date_1, self.date_2, self.date_1, self.date_2]
        self.transactions = [
            self.api.post_transaction(user_id, amount, date)
            for user_id, amount, date
            in zip(users_id, amounts, dates)
        ]
        for transaction in self.transactions:
            self.api.get_transaction(transaction['id'])

    def test_query_empty(self):
        j = self.api.query()
        assert get_ids(j['transactions']) == get_ids(self.transactions)
        assert j['sum'] == 90

    def test_query_user(self):
        j = self.api.query(user=self.user_id_1)
        assert get_ids(j['transactions']) == get_ids(self.transactions[:3])
        assert j['sum'] == 0

    def test_query_date(self):
        j = self.api.query(date=self.date_2)
        assert get_ids(j['transactions']) == get_ids([self.transactions[2], self.transactions[4]])
        assert j['sum'] == 20

    def test_query_type(self):
        j = self.api.query(type='outcome')
        assert get_ids(j['transactions']) == get_ids([self.transactions[2]])
        assert j['sum'] == -30
