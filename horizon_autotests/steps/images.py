"""
Images steps.

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

from ._utils import waiter
from .base import BaseSteps

CIRROS_URL = ('http://download.cirros-cloud.net/0.3.1/'
              'cirros-0.3.1-x86_64-uec.tar.gz')


class ImagesSteps(BaseSteps):
    """Images steps."""

    def page_images(self):
        """Open images page if it isn't opened."""
        return self._open(self.app.page_images)

    def create_image(self, image_name, image_url=CIRROS_URL,
                     disk_format='QCOW2', check=True):
        """Step to create image."""
        page_images = self.page_images()
        page_images.button_create_image.click()

        with page_images.form_create_image as form:
            form.field_name.value = image_name
            form.field_image_url.value = image_url
            form.field_disk_format.value = disk_format
            form.submit()

        page_images.spinner.wait_for_absence()

        if check:
            self.close_notification('success')

            with page_images.table_images.row(name=image_name) as row:
                row.wait_for_presence()
                with row.cell('status') as cell:
                    waiter.exe(60, lambda: cell.value == 'Active')

    def delete_image(self, image_name):
        """Step to delete image."""
        page_images = self.page_images()

        with page_images.table_images.row(
                name=image_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_images.form_confirm.submit()
        page_images.spinner.wait_for_absence()
        self.close_notification('success')

        page_images.table_images.row(
            name=image_name).wait_for_absence(60)

    def delete_images(self, image_names, check=True):
        """Step to delete images."""
        page_images = self.page_images()

        for image_name in image_names:
            page_images.table_images.row(
                name=image_name).checkbox.select()

        page_images.button_delete_images.click()
        page_images.form_confirm.submit()
        page_images.spinner.wait_for_absence()
        self.close_notification('success')

        if check:
            for image_name in image_names:
                page_images.table_images.row(
                    name=image_name).wait_for_absence(60)
