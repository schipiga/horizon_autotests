from horizon_autotests.app.pages import VolumesPage
from horizon_autotests.pom.utils import Waiter

from .base import BaseSteps

waiter = Waiter(polling=0.1)


class VolumesSteps(BaseSteps):

    @property
    def volumes_page(self):
        return self._open(VolumesPage)

    def create_volume(self, name, source_type='Image'):
        self.volumes_page.create_volume_button.click()
        with self.volumes_page.create_volume_form as form:
            form.name_field.value = name
            form.source_type_combobox.value = source_type
            image_sources = form.image_source_combobox.values
            form.image_source_combobox.value = image_sources[-1]
            volume_types = form.volume_type_combobox.values
            form.volume_type_combobox.value = volume_types[-1]
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('info')

        cell = self.volumes_page.volumes_table.row(name=name).cell('status')
        assert waiter.exe(60, lambda: cell.value == 'Available')

    def delete_volume(self, name):
        with self.volumes_page.volumes_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_item.click()
        self.volumes_page.delete_volume_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        assert waiter.exe(30, lambda: not row.is_present)

    def edit_volume(self, name, new_name):
        self.volumes_page.volumes_table.row(name=name).edit_volume_item.click()
        self.volumes_page.edit_volume_form.name_field.value = new_name
        self.volumes_page.edit_volume_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
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
        self.volumes_page.delete_volume_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        for row in rows:
            assert waiter.exe(10, lambda: not row.is_present)
