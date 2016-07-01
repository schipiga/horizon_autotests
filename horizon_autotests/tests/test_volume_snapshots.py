import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_edit_volume_snapshot(self, snapshot, volumes_steps):
        new_snapshot_name = snapshot.name + '(updated)'
        with snapshot.put(name=new_snapshot_name):
            volumes_steps.update_snapshot(snapshot.name, new_snapshot_name)

    def test_volume_snapshots_pagination(self):
        pass

    def test_create_volume_from_snapshot(self):
        pass
