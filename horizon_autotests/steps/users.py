"""
Users steps.

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

from horizon_autotests.app.pages import PageUsers

from .base import BaseSteps


class UsersSteps(BaseSteps):
    """Users steps."""

    def page_users(self):
        """Open users page if it isn't opened."""
        return self._open(PageUsers)

    def create_user(self, username, password, project=None):
        """Step to create user."""
        page_users = self.page_users()

        page_users.button_create_user.click()
        with page_users.form_create_user as form:

            form.field_name.value = username
            form.field_password.value = password
            form.field_confirm_password.value = password

            if project:
                form.combobox_project.value = project
            form.submit()

        page_users.spinner.wait_for_absence()
        self.close_notification('success')

        page_users.table_users.row(name=username).wait_for_presence()

    def delete_user(self, username):
        """Step to delete user."""
        page_users = self.page_users()

        with page_users.table_users.row(name=username).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_users.form_confirm.submit()
        page_users.spinner.wait_for_absence()

        self.close_notification('success')

        page_users.table_users.row(name=username).wait_for_absence()

    def delete_users(self, *usernames):
        """Step to delete users."""
        page_users = self.page_users()

        for username in usernames:
            page_users.table_users.row(name=username).checkbox.select()
        page_users.button_delete_users.click()
        page_users.form_confirm.submit()
        page_users.spinner.wait_for_absence()
        self.close_notification('success')

        for username in usernames:
            page_users.table_users.row(name=username).wait_for_absence()

    def change_user_password(self, username, new_password):
        """Step to change user password."""
        page_users = self.page_users()

        with page_users.table_users.row(name=username).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_change_password.click()

        with page_users.form_change_password as form:
            form.field_password.value = new_password
            form.field_confirm_password.value = new_password
            form.submit()

        page_users.spinner.wait_for_absence()
        self.close_notification('success')
