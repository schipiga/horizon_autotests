import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_dashboard_help_url(self):
        pass

    def test_password_change(self):
        pass

    def test_show_message_after_logout(self):
        pass

    def test_user_settings_change(self):
        pass
