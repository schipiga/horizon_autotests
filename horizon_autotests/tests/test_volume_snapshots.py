import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_edit_volume_snapshot(self):
        pass

    def test_volume_snapshots_pagination(self):
        pass

    def test_create_volume_from_snapshot(self):
        pass
