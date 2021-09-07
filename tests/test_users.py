from client import API
from pytest import fixture


class TestUsers:
    
    api = API()

    @fixture(autouse=True)
    def set_up(self):
        self.api.reset()

    def test_user_create(self):
        self.api.post_user('First1', 'Last1', 'test1@test.test', return_value=False)

    def test_user_read(self):
        j = self.api.post_user('First2', 'Last2', 'test2@test.test')
        self.api.get_user(j['id'], return_value=False)

    def test_user_update(self):
        j = self.api.post_user('First3', 'Last3', 'test3@test.test')
        self.api.patch_user(
            uuid=j['id'],
            first_name='First3_updated',
            last_name='Last3_updated',
            email='test3_updated@test.test',
            return_value=False,
        )
        j = self.api.get_user(j['id'])
        assert j['first_name'] == 'First3_updated'
        assert j['last_name'] == 'Last3_updated'
        assert j['email'] == 'test3_updated@test.test'

    def test_user_delete(self):
        j = self.api.post_user('First4', 'Last4', 'test4@test.test')
        self.api.delete_user(uuid=j['id'], return_value=False)
        self.api.get_user(j['id'], expected_status=404, return_value=False,)
