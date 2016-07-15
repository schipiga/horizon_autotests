"""
Networks steps.

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

from .base import BaseSteps


class NetworksSteps(BaseSteps):
    """networks steps."""

    def page_networks(self):
        """Open networks page if it isn't opened."""
        return self._open(self.app.page_networks)

    def page_admin_networks(self):
        """Open admin networks page if it isn't opened."""
        return self._open(self.app.page_admin_networks)

    def create_network(self, network_name, shared=False, create_subnet=False,
                       check=True):
        """Step to create network."""
        page_networks = self.page_networks()
        page_networks.button_create_network.click()

        with page_networks.form_create_network as form:
            form.field_name.value = network_name

            if shared:
                form.checkbox_shared.select()
            else:
                form.checkbox_shared.unselect()

            if create_subnet:
                form.checkbox_create_subnet.select()
            else:
                form.checkbox_create_subnet.unselect()

            form.submit()
        page_networks.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            page_networks.table_networks.row(
                name=network_name).wait_for_presence()

    def delete_network(self, network_name, check=True):
        """Step to delete network."""
        page_networks = self.page_networks()

        with page_networks.table_networks.row(
                name=network_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_networks.form_confirm.submit()
        page_networks.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            page_networks.table_networks.row(
                name=network_name).wait_for_absence()

    def delete_networks(self, network_names, check=True):
        """Step to delete networks as batch."""
        page_networks = self.page_networks()

        for network_name in network_names:
            page_networks.table_networks.row(
                name=network_name).checkbox.select()

        page_networks.button_delete_networks.click()
        page_networks.form_confirm.submit()
        page_networks.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            for network_name in network_names:
                page_networks.table_networks.row(
                    name=network_name).wait_for_absence()

    def add_subnet(self, network_name, subnet_name,
                   network_address='10.109.3.0/24', check=True):
        """Step to add subnet for network."""
        page_networks = self.page_networks()

        with page_networks.table_networks.row(
                name=network_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_add_subnet.click()

        with page_networks.form_add_subnet as form:
            form.field_name.value = subnet_name
            form.field_network_address.value = network_address
            form.button_next.click()
            form.submit()

        page_networks.spinner.wait_for_absence()

        if check:
            page_network = self.app.page_network
            self.close_notification('success')
            with page_network.table_subnets.row(name=subnet_name) as row:
                row.wait_for_presence()
                assert row.cell('network_address').value == network_address

    def admin_delete_network(self, network_name, check=True):
        """Step to delete network as admin."""
        page_networks = self.page_admin_networks()

        with page_networks.table_networks.row(
                name=network_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_networks.form_confirm.submit()
        page_networks.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            page_networks.table_networks.row(
                name=network_name).wait_for_absence()
