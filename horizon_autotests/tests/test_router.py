import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_create_router(self, create_router):
        create_router()
