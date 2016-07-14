"""
Containers page.

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

from horizon_autotests.app import ui as _ui

from .base import PageBase


@ui.register_ui(
    checkbox_public=_ui.CheckBox(By.NAME, 'public'),
    field_name=ui.TextField(By.NAME, 'name'))
class FormCreateContainer(_ui.Form):
    """Form to create container."""


@ui.register_ui(
    button_delete_container=ui.Button(
        By.CSS_SELECTOR, '[ng-click*="deleteContainer"]'))
class RowContainer(ui.Row):
    """Row with container."""


class ListContainers(ui.List):
    """List of containers."""

    row_cls = RowContainer
    row_xpath = ".//div[contains(@ng-repeat, 'container')]"


@ui.register_ui(
    button_create_container=ui.Button(
        By.CSS_SELECTOR, 'button[ng-click="cc.createContainer()"]'),
    form_create_container=FormCreateContainer(
        By.CSS_SELECTOR, 'div[ng-form="containerForm"]'),
    list_containers=ListContainers(
        By.CSS_SELECTOR, 'accordion.hz-container-accordion'))
class PageContainers(PageBase):
    """Containers Page."""

    url = "/project/containers/"
    navigate_items = 'Project', 'Object Store', 'Containers'
