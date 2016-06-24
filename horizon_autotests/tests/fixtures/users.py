import attrdict
import pytest

from horizon_autotests.steps import UsersSteps

from .utils import generate_ids

__all__ = [
    'create_users',
    'user',
    'users_steps'
]


@pytest.fixture
def users_steps(login, horizon):
    return UsersSteps(horizon)


@pytest.yield_fixture
def create_users(users_steps):
    users = []

    def _create_users(names):
        for name in names:
            users_steps.create_user(name, name, 'admin')
            users.append(attrdict.AttrDict(name=name, password=name))
        return users

    yield _create_users

    if users:
        users_steps.delete_users(*[user.name for user in users])


@pytest.fixture
def user(create_users):
    user_names = list(generate_ids('user'))
    return create_users(user_names)[0]
