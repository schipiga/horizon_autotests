import pytest

from .fixtures.utils import generate_ids


@pytest.mark.usefixtures('admin_only')
class TestAnyUser(object):

    def test_edit_volume_snapshot(self, snapshot, volumes_steps):
        new_snapshot_name = snapshot.name + '(updated)'
        with snapshot.put(name=new_snapshot_name):
            volumes_steps.update_snapshot(snapshot.name, new_snapshot_name)

    def test_volume_snapshots_pagination(self, volumes_steps, create_snapshots,
                                         update_settings):
        snapshot_names = list(generate_ids(prefix='snapshot', count=3))
        create_snapshots(snapshot_names)
        update_settings(items_per_page=1)

        tab_snapshots = volumes_steps.tab_snapshots()

        tab_snapshots.table_snapshots.row(
            name=snapshot_names[2]).wait_for_presence(30)
        assert tab_snapshots.table_snapshots.link_next.is_present
        assert not tab_snapshots.table_snapshots.link_prev.is_present

        tab_snapshots.table_snapshots.link_next.click()

        tab_snapshots.table_snapshots.row(
            name=snapshot_names[1]).wait_for_presence(30)
        assert tab_snapshots.table_snapshots.link_next.is_present
        assert tab_snapshots.table_snapshots.link_prev.is_present

        tab_snapshots.table_snapshots.link_next.click()

        tab_snapshots.table_snapshots.row(
            name=snapshot_names[0]).wait_for_presence(30)
        assert not tab_snapshots.table_snapshots.link_next.is_present
        assert tab_snapshots.table_snapshots.link_prev.is_present

        tab_snapshots.table_snapshots.link_prev.click()

        tab_snapshots.table_snapshots.row(
            name=snapshot_names[1]).wait_for_presence(30)
        assert tab_snapshots.table_snapshots.link_next.is_present
        assert tab_snapshots.table_snapshots.link_prev.is_present

        tab_snapshots.table_snapshots.link_prev.click()

        tab_snapshots.table_snapshots.row(
            name=snapshot_names[2]).wait_for_presence(30)
        assert tab_snapshots.table_snapshots.link_next.is_present
        assert not tab_snapshots.table_snapshots.link_prev.is_present

    def test_create_volume_from_snapshot(self):
        pass
