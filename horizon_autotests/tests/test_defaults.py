import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_update_defaults(self, update_defaults):
        update_defaults('volumes quota')
