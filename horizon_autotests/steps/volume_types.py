from horizon_autotests.app.pages import AdminVolumesPage

from .base import BaseSteps


class VolumeTypesSteps(BaseSteps):

    def volume_types_page(self):
        admin_volume_page = self._open(AdminVolumesPage)
        admin_volume_page.volume_types_tab.click()
        return admin_volume_page

    def create_volume_type(self, name, description=None):
        page = self.volume_types_page()
        page.create_volume_type_button.click()
        with page.create_volume_type_form as form:
            form.name_field.value = name
            if description:
                form.description_field.value = description
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        page.volume_types_table.row(
            name=name).wait_for_presence()

    def delete_volume_type(self, name):
        page = self.volume_types_page()
        with page.volume_types_table.row(
                name=name).dropdown_actions as actions:
            actions.toggle_button.click()
            actions.delete_item.click()
        page.confirm_delete_volume_types_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')
        page.volume_types_table.row(
            name=name).wait_for_absence()

    def delete_volume_types(self, *names):
        page = self.volume_types_page()
        for name in names:
            page.volume_types_table.row(
                name=name).checkbox.click()
        page.delete_volume_types_button.click()
        page.confirm_delete_volume_types_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        for name in names:
            page.volume_types_table.row(
                name=name).wait_for_absence()

    def create_qos_spec(self, name, consumer=None):
        page = self.volume_types_page()
        page.create_qos_spec_button.click()
        with page.create_qos_spec_form as form:
            form.name_field.value = name
            if consumer:
                form.consumer_field.value = consumer
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        page.qos_specs_table.row(name=name).wait_for_presence()

    def delete_qos_spec(self, name):
        page = self.volume_types_page()
        with page.qos_specs_table.row(
                name=name).dropdown_actions as actions:
            actions.toggle_button.click()
            actions.delete_item.click()
        page.confirm_delete_qos_specs_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')
        page.qos_specs_table.row(
            name=name).wait_for_absence()
