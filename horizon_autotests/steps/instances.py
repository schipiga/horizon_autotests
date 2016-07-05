from pom.utils import Waiter
from six import moves

from horizon_autotests.app.pages import InstancesPage

from .base import BaseSteps

waiter = Waiter(polling=0.1)


class InstancesSteps(BaseSteps):

    @property
    def instances_page(self):
        return self._open(InstancesPage)

    def create_instance(self, name, count=1):
        self.instances_page.launch_instance_button.click()
        with self.instances_page.launch_instance_form as form:

            with form.details_tab as tab:
                tab.name_field.value = name
                tab.count_field.value = count

            form.source_item.click()
            with form.source_tab as tab:
                tab.boot_source_field.value = 'Image'
                tab.volume_create_radio.value = 'No'
                tab.available_sources_table.row(
                    name='TestVM').add_button.click()

            form.flavor_item.click()
            with form.flavor_tab as tab:
                tab.available_flavors_table.row(
                    name='m1.tiny').add_button.click()

            form.network_item.click()
            with form.network_tab as tab:
                tab.available_networks_table.row(
                    name='admin_internal_net').add_button.click()

            form.submit()

        for i in moves.range(1, count + 1):
            if count == 1:
                instance_name = name
            else:
                instance_name = '{}-{}'.format(name, i)
            self.instances_page.instances_table.row(
                name=instance_name).wait_for_presence(30)
            cell = self.instances_page.instances_table.row(
                name=instance_name).cell('status')
            assert waiter.exe(300, lambda: cell.value == 'Active')

    def delete_instances(self, *instance_names):
        for instance_name in instance_names:
            self.instances_page.instances_table.row(
                name=instance_name).checkbox.select()

        self.instances_page.delete_instances_button.click()
        self.instances_page.delete_instance_confirm_form.submit()

        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        for instance_name in instance_names:
            self.instances_page.instances_table.row(
                name=instance_name).wait_for_absence(120)

    def delete_instance(self, name):
        with self.instances_page.instances_table.row(
                name=name).dropdown_actions as actions:
            actions.toggle_button.click()
            actions.delete_item.click()
        self.instances_page.delete_instance_confirm_form.submit()

        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        self.instances_page.instances_table.row(name=name).wait_for_absence(60)

    def lock_instance(self, name):
        with self.instances_page.instances_table.row(
                name=name).dropdown_actions as actions:
            actions.toggle_button.click()
            actions.lock_item.click()
        self.close_notification('success')

    def unlock_instance(self, name):
        with self.instances_page.instances_table.row(
                name=name).dropdown_actions as actions:
            actions.toggle_button.click()
            actions.unlock_item.click()
        self.close_notification('success')
