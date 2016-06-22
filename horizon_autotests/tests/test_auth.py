import pytest


@pytest.mark.usefixtures('any_user')
def test_login(login):
    pass
