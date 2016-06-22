import pytest

from .utils import generate_ids


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_edit_volume(self, volume, volumes_steps):
        new_name = volume.name + ' (updated)'
        volumes_steps.edit_volume(name=volume.name, new_name=new_name)
        volume.name = new_name

    @pytest.mark.parametrize('volumes_count', [1, 2])
    def test_delete_volumes(self, volumes_count, volumes_steps,
                            create_volumes):
        volume_names = list(generate_ids(prefix='volume', count=volumes_count))
        create_volumes(volume_names)


# def test_volumes_pagination(volumes_steps, create_volumes, update_settings):
#     volume_names = list(generate_ids(prefix='volume', count=3))
#     create_volumes(volume_names)
#     update_settings(ipp=1)

#     assert volumes_steps.volumes_page.next_link.is_present
#     assert not volumes_steps.volumes_page.prev_link.is_present

#     volumes_steps.volumes_page.next_link.click()

#     assert volumes_steps.volumes_page.next_link.is_present
#     assert volumes_steps.volumes_page.prev_link.is_present

#     volumes_steps.volumes_page.next_link.click()

#     assert not volumes_steps.volumes_page.next_link.is_present
#     assert volumes_steps.volumes_page.prev_link.is_present


# def test_view_volume(volume, volumes_steps):
#     volumes_steps.view_volume(volume.name)
#     assert volumes_steps.get_volume_info().get('name') == volume.name


# def test_change_volume_type(volume, volumes_steps):
#     volumes_steps.change_volume_type(volume.name)


# def test_upload_volume_to_image(volume, images_steps, volumes_steps):
#     image_name = generate_ids(prefix='image').next()
#     volumes_steps.upload_volume_to_image(image_name)
#     assert images_steps.images_table.row(name=image_name).is_present


# def test_volume_extend(volume, volumes_steps):
#     volumes_steps.extend_volume(volume.name)


# def test_change_volume_status(volume, volumes_steps):
#     volumes_steps.change_volume_status(volume.name)


# def test_launch_volume_as_instance(volume, instances_steps, volumes_steps):
#     instance_name = generate_ids('instance').next()
#     volumes_steps.launch_volume_as_instance(volume.name, instance_name)
#     with instances_steps.instances_page.instances_table as table:
#         assert table.row(name=instance_name).is_present


# def test_manage_volume_attachments(volume, instance, volumes_steps):
#     volumes_steps.attach_volume_to_instance(volume.name, instance.name)
#     volumes_steps.detach_volume_from_instance(volume.name, instance.name)


# def test_transfer_volume(volume, auth_steps, volumes_steps):
#     transfer_id, transfer_key = volumes_steps.transfer_volume(volume.name)
#     auth_steps.logout()
#     auth_steps.login('user', 'user')
#     volumes_steps.accept_transfer(transfer_id, transfer_key)
#     auth_steps.logout()
#     auth_steps.login('admin', 'admin')


# def test_migrate_volume(volume, volumes_steps):
#     volumes_steps.migrate_volume(volume.name)
#     volumes_steps.migrate_volume(volume.name)
