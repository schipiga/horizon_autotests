"""
Projects steps.

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


class ProjectsSteps(BaseSteps):
    """Projects steps."""

    def page_projects(self):
        """Open projects page if it isn't opened."""
        return self._open(self.app.page_projects)

    def create_project(self, project_name, check=True):
        """Step to create project."""
        page_projects = self.page_projects()
        page_projects.button_create_project.click()

        with page_projects.form_create_project as form:
            form.field_name.value = project_name
            form.submit()

        page_projects.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            page_projects.table_projects.row(
                name=project_name).wait_for_presence()

    def delete_project(self, project_name, check=True):
        """Step to delete project.
        """
        page_projects = self.page_projects()

        with page_projects.table_projects.row(
                name=project_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        page_projects.form_confirm.submit()
        page_projects.spinner.wait_for_absence()

        if check:
            self.close_notification('success')
            page_projects.table_projects.row(
                name=project_name).wait_for_absence()
