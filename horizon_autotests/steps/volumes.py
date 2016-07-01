from horizon_autotests.app.pages import (AdminVolumesPage,
                                         VolumePage,
                                         VolumesPage)
from horizon_autotests.pom.utils import Waiter

from .base import BaseSteps

waiter = Waiter(polling=0.1)


class VolumesSteps(BaseSteps):

    @property
    def volumes_page(self):
        return self._open(VolumesPage)

    def create_volume(self, name, source_type='Image', volume_type=0):
        self.volumes_page.create_volume_button.click()
        with self.volumes_page.create_volume_form as form:
            form.name_field.value = name
            form.source_type_combobox.value = source_type
            image_sources = form.image_source_combobox.values
            form.image_source_combobox.value = image_sources[-1]
            if volume_type is not None:
                if not volume_type:
                    volume_type = form.volume_type_combobox.values[-1]
                form.volume_type_combobox.value = volume_type
            form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        cell = self.volumes_page.volumes_table.row(name=name).cell('status')
        assert waiter.exe(60, lambda: cell.value == 'Available')

    def delete_volume(self, name):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_item.click()
        self.volumes_page.confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        assert waiter.exe(30, lambda: not row.is_present)

    def edit_volume(self, name, new_name):
        self.volumes_page.volumes_table.row(name=name).edit_volume_item.click()
        self.volumes_page.edit_volume_form.name_field.value = new_name
        self.volumes_page.edit_volume_form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        row = self.volumes_page.volumes_table.row(name=new_name)
        assert waiter.exe(30, lambda: row.is_present)

    def delete_volumes(self, *volume_names):
        rows = []
        for volume_name in volume_names:
            row = self.volumes_page.volumes_table.row(name=volume_name)
            rows.append(row)
            row.checkbox.select()
        self.volumes_page.delete_volumes_button.click()
        self.volumes_page.confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        for row in rows:
            assert waiter.exe(60, lambda: not row.is_present)

    @property
    def volume_page(self):
        return VolumePage(self.app)

    def view_volume(self, volume_name):
        self.volumes_page.volumes_table.row(
            name=volume_name).volume_link.click()
        assert self.volume_page.volume_info.name_label.value == volume_name

    def change_volume_type(self, name, volume_type=None):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.change_volume_type_item.click()
        with self.volumes_page.change_volume_type_form as form:
            if not volume_type:
                volume_type = form.volume_type_combobox.values[-1]
            form.volume_type_combobox.value = volume_type
            form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        cell = self.volumes_page.volumes_table.row(name=name).cell('type')
        assert waiter.exe(30, lambda: cell.value == volume_type)

    def upload_volume_to_image(self, name, image_name):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.upload_to_image_item.click()
        with self.volumes_page.upload_to_image_form as form:
            form.image_name_field.value = image_name
            form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        cell = self.volumes_page.volumes_table.row(name=name).cell('status')
        assert waiter.exe(90, lambda: cell.value == 'Available')

    def extend_volume(self, name, new_size=2):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.extend_volume_item.click()
        with self.volumes_page.extend_volume_form as form:
            form.new_size_field.value = new_size
            form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        cell = self.volumes_page.volumes_table.row(name=name).cell('size')
        assert waiter.exe(90, lambda: cell.value.startswith(str(new_size)))

    @property
    def admin_volumes_page(self):
        return self._open(AdminVolumesPage)

    def change_volume_status(self, name, status=None):
        with self.admin_volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.update_volume_status_item.click()

        with self.admin_volumes_page.update_volume_status_form as form:
            if not status:
                status = form.status_combobox.values[-1]
            form.status_combobox.value = status
            form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        cell = self.admin_volumes_page.volumes_table.row(
            name=name).cell('status')
        assert waiter.exe(90, lambda: cell.value == status)

    def launch_volume_as_instance(self, name, instance_name, count=1):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.launch_volume_as_instance_item.click()

        with self.volumes_page.launch_instance_form as form:

            with form.details_tab as tab:
                tab.name_field.value = instance_name
                tab.count_field.value = count

            form.flavor_item.click()
            with form.flavor_tab as tab:
                tab.available_flavors_table.row(
                    name='m1.tiny').add_button.click()

            form.network_item.click()
            with form.network_tab as tab:
                tab.available_networks_table.row(
                    name='admin_internal_net').add_button.click()

            form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)

    def attach_instance(self, volume_name, instance_name):
        with self.volumes_page.volumes_table.row(name=volume_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.manage_attachments_item.click()

        with self.volumes_page.manage_attachments_form as form:
            instance_value = next(val for val in form.instance_combobox.values
                                  if instance_name in val)
            form.instance_combobox.value = instance_value
            form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        with row.cell('status') as cell:
            assert waiter.exe(60, cell.value == 'In-use')

        assert instance_name in row.cell('attached_to').value

    def detach_instance(self, volume_name, instance_name):
        with self.volumes_page.volumes_table.row(name=volume_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.manage_attachments_item.click()

        with self.volumes_page.manage_attachments_form as form:
            form.instances_table.row(
                name=instance_name).detach_volume_button.click()

        self.volumes_page.confirm_form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        with row.cell('status') as cell:
            assert waiter.exe(60, cell.value == 'Available')

    def create_transfer(self, volume_name, transfer_name):
        with self.volumes_page.volumes_table.row(name=volume_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.create_transfer_item.click()

        with self.volumes_page.create_transfer_form as form:
            form.transfer_name_field.value = transfer_name
            form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        with self.volume_transfer_page.transfer_info_form as form:
            transfer_id = form.transfer_id_field.value
            transfer_key = form.transfer_key_field.value

        assert row.cell('status').value == 'awaiting-transfer'

        return transfer_id, transfer_key

    def accept_transfer(self, transfer_id, transfer_key, volume_name):
        self.volumes_page.accept_transfer_button.click()

        with self.volumes_page.accept_transfer_form as form:
            form.transfer_id_field.value = transfer_id
            form.transfer_key_field.value = transfer_key
            form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        with self.volumes_page.volumes_table.row(name=volume_name) as row:
            row.wait_for_presence(30)
            row.cell('status').value == 'Available'

    def migrate_host(self, volume_name, new_host=None):
        with self.admin_volumes_page.volumes_table.row(
                name=volume_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.migrate_volume_item.click()

        with self.admin_volumes_page.migrate_volume_form as form:
            old_host = form.current_host_field.value
            if not new_host:
                new_host = form.destination_host_combobox.values[-1]
            form.destination_host_combobox.value = new_host
            form.submit()

        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        return old_host, new_host

    def snapshots_tab(self):
        self.volumes_page.snapshots_label.click()
        return self.volumes_page.snapshots_tab

    def create_snapshot(self, volume_name, snapshot_name, description=None):
        with self.volumes_page.volumes_table.row(name=volume_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.create_snapshot_item.click()

        with self.volumes_page.create_snapshot_form as form:
            form.snapshot_name_field.value = snapshot_name
            if description is not None:
                self.description_field.value = description
            form.submit()

        snapshots_tab = self.snapshots_tab()

        with snapshots_tab.snapshots_table.row(name=snapshot_name) as row:
            assert row.is_present
            with row.cell('status') as cell:
                assert waiter.exe(30, cell.value == 'Available')

    def delete_snapshot(self, snapshot_name):
        snapshots_tab = self.snapshots_tab()

        with snapshots_tab.snapshots_table.row(name=snapshot_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_snapshot_item.click()

        snapshots_tab.confirm_form.submit()
        snapshots_tab.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        row.wait_for_absence(30)

    def update_snapshot(self, snapshot_name, new_snapshot_name,
                        description=None):
        snapshots_tab = self.snapshots_tab()

        with snapshots_tab.snapshots_table.row(
                name=snapshot_name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.edit_snapshot_item.click()

        with snapshots_tab.edit_snapshot_form as form:
            form.snapshot_name_field.value = new_snapshot_name
            if description is not None:
                form.description_field.value = description
            form.submit()

        snapshots_tab.modal_spinner.wait_for_absence(30)
        self.close_notification('info')

        with snapshots_tab.snapshots_table.row(name=new_snapshot_name) as row:
            assert row.is_present
            with row.cell('status') as cell:
                assert waiter.exe(30, cell.value == 'Available')
