import pytest

from .fixtures.config import ADMIN_NAME, ADMIN_PASSWD
from .fixtures.utils import generate_ids


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    @pytest.mark.parametrize('users_count', [1, 2])
    def test_delete_users(self, users_count, create_users):
        user_names = list(generate_ids('user', count=users_count))
        create_users(user_names)

    def test_change_user_password(self, user, users_steps, auth_steps):
        new_password = 'new-' + user.password
        users_steps.change_user_password(user.name, new_password)
        user.password = new_password
        auth_steps.logout()
        auth_steps.login(user.name, user.password)
        auth_steps.logout()
        auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
