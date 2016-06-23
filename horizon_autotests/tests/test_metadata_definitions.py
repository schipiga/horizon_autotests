import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_create_namespace(self, create_namespace):
        create_namespace()
