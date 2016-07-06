"""
Predefined UI components for page or tab.

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

from pom import ui
from selenium.webdriver.common.by import By

from .form import Form


@ui.register_ui(
    item_exit=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))
class DropdownMenuAccount(ui.Block):
    """Dropdown menu for account settings."""


class DropdownMenuProject(ui.Block):
    """Dropdown menu for project switching."""

    def item_project(self, name):
        """Get project item from from dropdown list."""
        selector = (
            './/ul[contains(@class, "dropdown-menu")]/li//span[contains('
            '@class, "dropdown-title") and contains(., "{}")]'.format(name))

        item = ui.UI(By.XPATH, selector)
        item.container = self
        return item


class Spinner(ui.UI):
    """Spinner to wait loading."""

    def wait_for_absence(self, timeout=30):
        """Wait spinner absence with predefined timeout.

        Arguments:
            - timeout: integer, default is 30 sec.
        """
        super(Spinner, self).wait_for_absence(timeout)


@ui.register_ui(
    dropdown_menu_account=DropdownMenuAccount(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'),
    dropdown_menu_project=DropdownMenuProject(
        By.CSS_SELECTOR, 'ul.navbar-nav > li.dropdown'),
    form_confirm=Form(By.CSS_SELECTOR, 'div.modal-content > div.modal-footer'),
    spinner=ui.UI(By.CSS_SELECTOR, 'div.modal-dialog'))
class InitiatedUI(ui.Container):
    """Predefined UI components for page or tab."""
