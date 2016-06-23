import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_create_keypair(self, create_keypair):
        create_keypair()

    def test_import_keypair(self, import_keypair):
        import_keypair()
