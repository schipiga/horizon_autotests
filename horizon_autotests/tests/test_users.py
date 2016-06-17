import pytest


@pytest.fixture
def username():
    return 'username'


@pytest.fixture
def password():
    return 'password'


def test_create_user(users_steps, username, password):
    users_steps.create_user(username, password)
    users_steps.delete_user(username)
