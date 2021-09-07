from client import API
from pytest import fixture
from utils import post_user


class TestTransactions:

    api = API()

    def post_user(self, number: int):
        return post_user(self.api, 'transaction', number)

    @fixture(autouse=True)
    def set_up(self):
        self.api.reset()
        self.user_1, self.user_2 = self.post_user(1), self.post_user(2)

    def test_transaction_create(self):
        self.api.post_transaction(self.user_1['id'], 1, '2021-05-11', return_value=False)

    def test_transaction_read(self):
        j = self.api.post_transaction(self.user_1['id'], 2, '2021-05-11')
        self.api.get_transaction(j['id'], return_value=False)

    def test_transaction_update(self):
        j = self.api.post_transaction(self.user_1['id'], 3, '2021-05-11')
        self.api.patch_transaction(
            uuid=j['id'],
            user_id=self.user_2['id'],
            amount=4,
            date='2021-05-12'
        )
        j = self.api.get_transaction(j['id'])
        assert j['user_id'] == self.user_2['id']
        assert j['amount'] == 4
        assert j['date'] == '2021-05-12'

    def test_user_delete(self):
        j = self.api.post_transaction(self.user_1['id'], 5, '2021-05-11')
        self.api.delete_transaction(uuid=j['id'], return_value=False)
        self.api.get_transaction(j['id'], expected_status=404, return_value=False)
