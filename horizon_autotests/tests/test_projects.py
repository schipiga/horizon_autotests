import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_create_project(self):
        pass
