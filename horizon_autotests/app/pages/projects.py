from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'),
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'))
class ProjectsRow(ui.Row):
    pass


class ProjectsTable(ui.Table):
    columns = {'name': 2}
    Row = ProjectsRow


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'))
class CreateProjectForm(_ui.Form):
    submit_locator = By.CSS_SELECTOR, 'input.btn.btn-primary'


@pom.register_ui(
    create_project_button=ui.Button(By.ID, 'tenants__action_create'),
    projects_table=ProjectsTable(By.ID, 'tenants'),
    create_project_form=CreateProjectForm(By.CSS_SELECTOR,
                                          'form[action*="identity/create"]'),
    delete_project_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'))
class ProjectsPage(BasePage):
    url = "/identity/"
