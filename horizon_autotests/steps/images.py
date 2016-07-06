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

from horizon_autotests.app.pages import PageImages

from .base import BaseSteps


class ImagesSteps(BaseSteps):
    """Images steps."""

    def page_images(self):
        """Open images page if it isn't opened."""
        return self._open(PageImages)

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
            name=image_name).wait_for_absence(30)
