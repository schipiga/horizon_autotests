import pytest
from pom.utils import Waiter

from .fixtures.config import DEMO_NAME, DEMO_PASSWD
from .fixtures.utils import generate_ids

waiter = Waiter(polling=0.1)


@pytest.mark.usefixtures('admin_only')
class TestAnyUser(object):

    def test_edit_volume(self, volume, volumes_steps):
        new_name = volume.name + ' (updated)'
        with volume.put(name=new_name):
            volumes_steps.edit_volume(volume_name=volume.name,
                                      new_volume_name=new_name)

    @pytest.mark.parametrize('volumes_count', [1, 2])
    def test_delete_volumes(self, volumes_count, volumes_steps,
                            create_volumes):
        volume_names = list(generate_ids(prefix='volume', count=volumes_count))
        create_volumes(volume_names)

    def test_volumes_pagination(self, volumes_steps, create_volumes,
                                update_settings):
        volume_names = list(generate_ids(prefix='volume', count=3))
        create_volumes(volume_names)
        update_settings(items_per_page=1)

        assert volumes_steps.volumes_page.volumes_table.row(
            name=volume_names[2]).is_present
        assert volumes_steps.volumes_page.next_link.is_present
        assert not volumes_steps.volumes_page.prev_link.is_present

        volumes_steps.volumes_page.next_link.click()

        assert volumes_steps.volumes_page.volumes_table.row(
            name=volume_names[1]).is_present
        assert volumes_steps.volumes_page.next_link.is_present
        assert volumes_steps.volumes_page.prev_link.is_present

        volumes_steps.volumes_page.next_link.click()

        assert volumes_steps.volumes_page.volumes_table.row(
            name=volume_names[0]).is_present
        assert not volumes_steps.volumes_page.next_link.is_present
        assert volumes_steps.volumes_page.prev_link.is_present

        volumes_steps.volumes_page.prev_link.click()

        assert volumes_steps.volumes_page.volumes_table.row(
            name=volume_names[1]).is_present
        assert volumes_steps.volumes_page.next_link.is_present
        assert volumes_steps.volumes_page.prev_link.is_present

        volumes_steps.volumes_page.prev_link.click()

        assert volumes_steps.volumes_page.volumes_table.row(
            name=volume_names[2]).is_present
        assert volumes_steps.volumes_page.next_link.is_present
        assert not volumes_steps.volumes_page.prev_link.is_present

    def test_view_volume(self, volume, volumes_steps):
        volumes_steps.view_volume(volume.name)

    def test_change_volume_type(self, create_volume, volumes_steps):
        volume_name = generate_ids('volume').next()
        create_volume(volume_name, volume_type=None)
        volumes_steps.change_volume_type(volume_name)

    def test_upload_volume_to_image(self, volume, images_steps, volumes_steps):
        image_name = generate_ids(prefix='image', length=20).next()
        volumes_steps.upload_volume_to_image(volume.name, image_name)
        assert images_steps.images_page.images_table.row(
            name=image_name).is_present
        images_steps.delete_image(image_name)

    def test_volume_extend(self, volume, volumes_steps):
        volumes_steps.extend_volume(volume.name)


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_change_volume_status(self, volume, volumes_steps):
        volumes_steps.change_volume_status(volume.name, 'Error')
        volumes_steps.change_volume_status(volume.name, 'Available')

    def test_launch_volume_as_instance(self, volume, instances_steps,
                                       volumes_steps):
        instance_name = generate_ids('instance').next()
        volumes_steps.launch_volume_as_instance(volume.name, instance_name)

        instances_steps.instances_page.instances_table.row(
            name=instance_name).wait_for_presence(30)
        cell = instances_steps.instances_page.instances_table.row(
            name=instance_name).cell('status')
        assert waiter.exe(60, lambda: cell.value == 'Active')

        instances_steps.delete_instance(instance_name)

    def test_manage_volume_attachments(self, volume, instance, volumes_steps):
        volumes_steps.attach_instance(volume.name, instance.name)
        volumes_steps.detach_instance(volume.name, instance.name)

    def test_transfer_volume(self, volume, auth_steps, volumes_steps):
        transfer_name = generate_ids('transfer').next()
        transfer_id, transfer_key = volumes_steps.create_transfer(
            volume.name, transfer_name)
        auth_steps.logout()
        auth_steps.login(DEMO_NAME, DEMO_PASSWD)
        volumes_steps.accept_transfer(transfer_id, transfer_key)

    def test_migrate_volume(self, volume, volumes_steps):
        old_host, _ = volumes_steps.migrate_volume(volume.name)
        volumes_steps.migrate_volume(volume.name, old_host)
