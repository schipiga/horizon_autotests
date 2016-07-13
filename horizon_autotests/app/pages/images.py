"""
Images page.

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
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=_ui.DropdownMenu())
class RowImage(ui.Row):
    """Row with image in images table."""


class TableImages(_ui.Table):
    """Images table."""

    columns = {'name': 2, 'type': 3, 'status': 4, 'format': 7}
    row_cls = RowImage


@ui.register_ui(
    field_disk_format=ui.ComboBox(By.NAME, 'disk_format'),
    field_image_file=ui.TextField(By.NAME, 'image_file'),
    field_image_url=ui.TextField(By.NAME, 'image_url'),
    field_name=ui.TextField(By.NAME, 'name'),
    field_source_type=ui.ComboBox(By.NAME, 'source_type'))
class FormCreateImage(_ui.Form):
    """Form to create image."""


@ui.register_ui(
    button_create_image=ui.Button(By.ID, 'images__action_create'),
    button_delete_images=ui.Button(By.ID, 'images__action_delete'),
    form_create_image=FormCreateImage(By.ID, 'create_image_form'),
    table_images=TableImages(By.ID, 'images'))
class PageImages(PageBase):
    """Images Page."""

    url = "/project/images/"
