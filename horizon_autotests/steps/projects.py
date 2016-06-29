from horizon_autotests.app.pages import ProjectsPage

from .base import BaseSteps


class ProjectsSteps(BaseSteps):

    @property
    def projects_page(self):
        return self._open(ProjectsPage)

    def create_project(self, name):
        self.projects_page.create_project_button.click()
        self.projects_page.create_project_form.name_field.value = name
        self.projects_page.create_project_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

    def delete_project(self, name):
        with self.projects_page.projects_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_item.click()
        self.projects_page.delete_project_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')
