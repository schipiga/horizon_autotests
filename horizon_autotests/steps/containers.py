"""
Containers steps.

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


class ContainersSteps(BaseSteps):
    """Containers steps."""

    def page_containers(self):
        """Open containers page if it isn't opened."""
        return self._open(self.app.page_containers)

    def create_container(self, container_name, public=False, check=True):
        """Step to create container."""
        page_containers = self.page_containers()
        page_containers.button_create_container.click()

        with page_containers.form_create_container as form:
            form.field_name.value = container_name

            if public:
                form.checkbox_public.select()
            else:
                form.checkbox_public.unselect()

            form.submit()

        if check:
            self.close_notification('success')
            page_containers.list_containers.row(
                container_name).wait_for_presence()

    def delete_container(self, container_name, check=True):
        """Step to delete container."""
        page_containers = self.page_containers()

        with page_containers.list_containers.row(container_name) as row:
            row.click()
            row.button_delete_container.click()

        page_containers.form_confirm.submit()

        if check:
            self.close_notification('success')
            page_containers.list_containers.row(
                container_name).wait_for_absence()
