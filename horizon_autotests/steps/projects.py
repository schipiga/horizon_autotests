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

from horizon_autotests.app.pages import PageProjects

from .base import BaseSteps


class ProjectsSteps(BaseSteps):
    """Projects steps."""

    def projects_page(self):
        """Open projects page if it isn't opened."""
        return self._open(PageProjects)

    def create_project(self, project_name):
        """Step to create project."""
        with self.projects_page() as page:
            page.button_create_project.click()

            page.form_create_project.field_name.value = project_name
            page.form_create_project.submit()

            page.spinner.wait_for_absence()

        self.close_notification('success')

    def delete_project(self, project_name):
        """Step to delete project.
        """
        projects_page = self.projects_page()

        with projects_page.table_projects.row(
                name=project_name).dropdown_menu as menu:
            menu.button_toggle.click()
            menu.item_delete.click()

        projects_page.form_confirm.submit()
        projects_page.spinner.wait_for_absence()

        self.close_notification('success')
