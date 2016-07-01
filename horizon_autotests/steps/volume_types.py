from horizon_autotests.app.pages import AdminVolumesPage

from .base import BaseSteps


class VolumeTypesSteps(BaseSteps):

    def tab_volume_types(self):
        admin_volume_page = self._open(AdminVolumesPage)
        admin_volume_page.label_volume_types.click()
        return admin_volume_page.tab_volume_types

    def create_volume_type(self, volume_type_name, description=None):
        tab = self.tab_volume_types()
        tab.button_create_volume_type.click()

        with tab.form_create_volume_type as form:
            form.field_name.value = volume_type_name
            if description:
                form.field_description.value = description
            form.submit()

        self.base_page.spinner.wait_for_absence()
        self.close_notification('success')

        tab.table_volume_types.row(name=volume_type_name).wait_for_presence()

    def delete_volume_type(self, volume_type_name):
        tab = self.tab_volume_types()

        with tab.table_volume_types.row(
                name=volume_type_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        tab.form_confirm.submit()
        self.base_page.spinner.wait_for_absence()
        self.close_notification('success')

        tab.table_volume_types.row(name=volume_type_name).wait_for_absence()

    def delete_volume_types(self, *volume_type_names):
        tab = self.tab_volume_types()

        for volume_type_name in volume_type_names:
            tab.table_volume_types.row(name=volume_type_name).checkbox.click()

        tab.button_delete_volume_types.click()
        tab.confirm_form.submit()

        self.base_page.spinner.wait_for_absence()
        self.close_notification('success')

        for volume_type_name in volume_type_names:
            tab.table_volume_types.row(
                name=volume_type_name).wait_for_absence()

    def create_qos_spec(self, qos_spec_name, consumer=None):
        tab = self.tab_volume_types()
        tab.button_create_qos_spec.click()

        with tab.form_create_qos_spec as form:
            form.field_name.value = qos_spec_name
            if consumer:
                form.field_consumer.value = consumer
            form.submit()

        self.base_page.spinner.wait_for_absence()
        self.close_notification('success')

        tab.table_qos_specs.row(name=qos_spec_name).wait_for_presence()

    def delete_qos_spec(self, qos_spec_name):
        tab = self.tab_volume_types()

        with tab.table_qos_specs.row(
                name=qos_spec_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        tab.form_confirm.submit()
        self.base_page.spinner.wait_for_absence()
        self.close_notification('success')

        tab.table_qos_specs.row(name=qos_spec_name).wait_for_absence()
