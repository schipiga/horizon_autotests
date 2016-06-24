import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_download_rc_v2(self, api_access_steps):
        api_access_steps.download_rc_v2()

    def test_download_rc_v3(self, api_access_steps):
        api_access_steps.download_rc_v3()

    def test_view_credentials(self, api_access_steps):
        api_access_steps.view_credentials()
