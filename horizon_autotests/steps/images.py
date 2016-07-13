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

    def create_image(self, image_name, image_url=CIRROS_URL, image_file=None,
                     disk_format='QCOW2', check=True):
        """Step to create image."""
        page_images = self.page_images()
        page_images.button_create_image.click()

        with page_images.form_create_image as form:
            form.field_name.value = image_name

            if image_file:
                form.field_source_type.value = 'Image File'
                form.field_image_file.value = image_file

            else:
                form.field_source_type.value = 'Image Location'
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

    def delete_image(self, image_name, check=True):
        """Step to delete image."""
        page_images = self.page_images()

        with page_images.table_images.row(
                name=image_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_images.form_confirm.submit()
        page_images.spinner.wait_for_absence()

        if check:
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

    def update_metadata(self, image_name, metadata, check=True):
        """Step to update image metadata."""
        page_images = self.page_images()
        with page_images.table_images.row(
                name=image_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_update_metadata.click()

        with page_images.form_update_metadata as form:
            for metadata_name, metadata_value in metadata.items():
                form.field_metadata_name.value = metadata_name
                form.button_add_metadata.click()
                form.list_metadata.row(
                    metadata_name).field_metadata_value.value = metadata_value

            form.submit()

        if check:
            page_images.modal.wait_for_absence()

            with page_images.table_images.row(name=image_name) as row:
                row.wait_for_presence()

                with row.cell('status') as cell:
                    waiter.exe(60, lambda: cell.value == 'Active')

    def get_metadata(self, image_name, check=True):
        """Step to get image metadata."""
        metadata = {}

        page_images = self.page_images()

        with page_images.table_images.row(
                name=image_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_update_metadata.click()

        for row in page_images.form_update_metadata.list_metadata.rows:
            metadata[row.field_metadata_name.value] = \
                row.field_metadata_value.value

        page_images.form_update_metadata.cancel()

        if check:
            page_images.modal.wait_for_absence()

        return metadata

    def update_image(self, image_name, new_image_name, check=True):
        """Step to update image."""
        page_images = self.page_images()
        with page_images.table_images.row(
                name=image_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_edit.click()

        with page_images.form_update_image as form:
            form.field_name.value = new_image_name
            form.submit()

        page_images.spinner.wait_for_absence()

        if check:
            self.close_notification('success')

            with page_images.table_images.row(name=new_image_name) as row:
                row.wait_for_presence()

                with row.cell('status') as cell:
                    waiter.exe(60, lambda: cell.value == 'Active')
