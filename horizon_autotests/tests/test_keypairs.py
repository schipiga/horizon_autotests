from os import path

import pytest

with open(path.join(path.dirname(__file__), 'test_data', 'key.pub')) as f:
    PUBLIC_KEY = f.read()


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_create_keypair(self, keypair):
        pass

    def test_import_keypair(self, import_keypair):
        import_keypair(PUBLIC_KEY)
