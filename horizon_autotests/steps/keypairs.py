"""
Keypairs steps.

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

from horizon_autotests.app.pages import PageAccess

from .base import BaseSteps


class KeypairsSteps(BaseSteps):
    """Keypairs steps."""

    def tab_keypairs(self):
        """Open keypairs tab."""
        with self._open(PageAccess) as page:
            page.label_keypairs.click()
            return page.tab_keypairs

    def create_keypair(self, keypair_name):
        """Step to create keypair."""
        tab_keypairs = self.tab_keypairs()
        tab_keypairs.button_create_keypair.click()

        with tab_keypairs.form_create_keypair as form:
            form.field_name.value = keypair_name
            form.submit()

        tab_keypairs.spinner.wait_for_absence()

        self.tab_keypairs().table_keypairs.row(
            name=keypair_name).wait_for_presence()

    def delete_keypair(self, keypair_name):
        """Step to delete keypair."""
        tab_keypairs = self.tab_keypairs()

        tab_keypairs.table_keypairs.row(
            name=keypair_name).button_delete_keypair.click()
        tab_keypairs.form_confirm.submit()

        tab_keypairs.spinner.wait_for_absence()
        self.close_notification('success')

        tab_keypairs.table_keypairs.row(
            name=keypair_name).wait_for_absence()

    def import_keypair(self, keypair_name, public_key):
        """Step to import keypair."""
        tab_keypairs = self.tab_keypairs()
        tab_keypairs.button_import_keypair.click()

        with tab_keypairs.form_import_keypair as form:
            form.field_name.value = keypair_name
            form.field_public_key.value = public_key
            form.submit()

        tab_keypairs.spinner.wait_for_absence()
        self.close_notification('success')

        tab_keypairs.table_keypairs.row(
            name=keypair_name).wait_for_presence()

    def delete_keypairs(self, *keypair_names):
        """Step to delete keypairs."""
        tab_keypairs = self.tab_keypairs()

        for keypair_name in keypair_names:
            tab_keypairs.table_keypairs.row(
                name=keypair_name).checkbox.select()

        tab_keypairs.button_delete_keypairs.click()
        tab_keypairs.form_confirm.submit()

        tab_keypairs.spinner.wait_for_absence()
        self.close_notification('success')

        for keypair_name in keypair_names:
            tab_keypairs.table_keypairs.row(
                name=keypair_name).wait_for_absence()
