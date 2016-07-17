"""
Instances steps.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from six import moves

from ._utils import waiter
from .base import BaseSteps


class InstancesSteps(BaseSteps):
    """Instances steps."""

    def page_instances(self):
        """Open instances page if it isn't opened."""
        return self._open(self.app.page_instances)

    def create_instance(self, name, count=1):
        """Step to create instance."""
        page_instances = self.page_instances()

        page_instances.button_launch_instance.click()
        with page_instances.form_launch_instance as form:

            with form.tab_details as tab:
                tab.field_name.value = name
                tab.field_count.value = count

            form.item_source.click()
            with form.tab_source as tab:
                tab.combobox_boot_source.value = 'Image'
                tab.radio_volume_create.value = 'No'
                tab.table_available_sources.row(
                    name='TestVM').button_add.click()

            form.item_flavor.click()
            with form.tab_flavor as tab:
                tab.table_available_flavors.row(
                    name='m1.tiny').button_add.click()

            form.item_network.click()
            with form.tab_network as tab:
                tab.table_available_networks.row(
                    name='admin_internal_net').button_add.click()

            form.submit()

        for i in moves.range(1, count + 1):
            if count == 1:
                instance_name = name
            else:
                instance_name = '{}-{}'.format(name, i)
            page_instances.table_instances.row(
                name=instance_name).wait_for_presence(30)
            cell = page_instances.table_instances.row(
                name=instance_name).cell('status')
            assert waiter.exe(300, lambda: cell.value == 'Active')

    def delete_instances(self, *instance_names):
        """Step to delete instances."""
        page_instances = self.page_instances()

        for instance_name in instance_names:
            page_instances.table_instances.row(
                name=instance_name).checkbox.select()

        page_instances.button_delete_instances.click()
        page_instances.form_confirm.submit()

        page_instances.spinner.wait_for_absence()
        self.close_notification('success')

        for instance_name in instance_names:
            page_instances.table_instances.row(
                name=instance_name).wait_for_absence(120)

    def delete_instance(self, instance_name):
        """Step to delete instance."""
        page_instances = self.page_instances()

        with page_instances.table_instances.row(
                name=instance_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_instances.form_confirm.submit()
        page_instances.spinner.wait_for_absence()
        self.close_notification('success')

        page_instances.table_instances.row(
            name=instance_name).wait_for_absence(60)

    def lock_instance(self, instance_name):
        """Step to lock instance."""
        with self.page_instances().table_instances.row(
                name=instance_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_lock.click()

        self.close_notification('success')

    def unlock_instance(self, instance_name):
        """Step to unlock instance."""
        with self.page_instances().table_instances.row(
                name=instance_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_unlock.click()

        self.close_notification('success')

    def view_instance(self, instance_name, check=True):
        """Step to view instance."""
        self.page_instances().table_instances.row(
            name=instance_name).link_instance.click()

        if check:
            assert self.app.page_instance.info_instance.label_name.value \
                == instance_name

    def filter_instances(self, query, check=True):
        """Step to filter instances."""
        page_instances = self.page_instances()

        page_instances.field_filter_instances.value = query
        page_instances.button_filter_instances.click()

        if check:

            def check_rows():
                for row in page_instances.table_instances.rows:
                    if not (row.is_present and
                            query in row.link_instance.value):
                        return False
                return True

            assert waiter.exe(10, check_rows)

    def reset_instances_filter(self):
        """Step to reset instances filter."""
        page_instances = self.page_instances()
        page_instances.field_filter_instances.value = ''
        page_instances.button_filter_instances.click()
