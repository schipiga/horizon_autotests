from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@ui.register_ui(
    item_change_password=ui.UI(By.CSS_SELECTOR,
                               '*[id*="action_change_password"]'))
class DropdownMenu(_ui.DropdownMenu):
    pass


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=DropdownMenu())
class RowUser(ui.Row):
    pass


class TableUsers(ui.Table):
    columns = {'name': 2, 'email': 4}
    Row = RowUser


@ui.register_ui(
    combobox_project=ui.ComboBox(By.NAME, 'project'),
    field_name=ui.TextField(By.NAME, 'name'),
    field_password=ui.TextField(By.NAME, 'password'),
    field_password_confirm=ui.TextField(By.NAME, 'confirm_password'))
class FormCreateUser(_ui.Form):
    pass


@ui.register_ui(
    field_confirm_password=ui.TextField(By.NAME, 'confirm_password'),
    field_password=ui.TextField(By.NAME, 'password'))
class FormChangePassword(_ui.Form):
    pass


@ui.register_ui(
    button_create_user=ui.Button(By.ID, 'users__action_create'),
    button_delete_users=ui.Button(By.ID, 'users__action_delete'),
    form_change_password=FormChangePassword(By.ID,
                                            'change_user_password_form'),
    form_create_user=FormCreateUser(By.ID, 'create_user_form'),
    table_users=TableUsers(By.ID, 'users'))
class UsersPage(BasePage):
    url = '/identity/users/'
