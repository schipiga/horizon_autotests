import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_volume_type_create(self, volume_type):
        pass

    def test_qos_spec_create(self, qos_spec):
        pass
