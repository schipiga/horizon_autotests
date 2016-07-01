from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=_ui.DropdownMenu())
class RowProject(ui.Row):
    pass


class TableProjects(ui.Table):
    columns = {'name': 2}
    Row = RowProject


@ui.register_ui(field_name=ui.TextField(By.NAME, 'name'))
class FormCreateProject(_ui.Form):
    submit_locator = By.CSS_SELECTOR, 'input.btn.btn-primary'


@ui.register_ui(
    button_create_project=ui.Button(By.ID, 'tenants__action_create'),
    form_create_project=FormCreateProject(By.CSS_SELECTOR,
                                          'form[action*="identity/create"]'),
    form_delete_project_confirm=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    table_projects=TableProjects(By.ID, 'tenants'))
class ProjectsPage(BasePage):
    url = "/identity/"
