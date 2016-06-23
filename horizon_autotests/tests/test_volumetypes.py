import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_volume_type_create(self):
        pass

    def test_qos_spec_create(self):
        pass
