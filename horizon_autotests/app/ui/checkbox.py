"""
Themable checkbox.

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


class CheckBox(ui.CheckBox):
    """Themable checkbox."""

    @property
    def label(self):
        """Label of checkbox."""
        web_id = self.webelement.get_attribute('id')
        label_locator = By.CSS_SELECTOR, 'label[for="{}"]'.format(web_id)
        return self.container.find_element(label_locator)

    def select(self):
        """Select checkbox if it isn't selected."""
        if not self.is_selected:
            self.label.click()

    def unselect(self):
        """Unselect checkbox if it is selected."""
        if self.is_selected:
            self.label.click()
