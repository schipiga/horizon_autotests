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


def test_delete_users(users_steps, username, password):
    users_steps.create_user(username, password)
    users_steps.delete_users(username)


def test_change_user_password(users_steps, username, password):
    users_steps.create_user(username, password)
    users_steps.change_user_password(username, 'new-' + password)
    users_steps.delete_users(username)
