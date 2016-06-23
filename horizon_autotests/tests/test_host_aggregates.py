import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_host_aggregate_create(self, host_aggregate):
        pass
