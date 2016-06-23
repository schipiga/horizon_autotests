import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_create_security_group(self, create_security_group):
        create_security_group()
