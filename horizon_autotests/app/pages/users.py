from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'),
    change_password_item=ui.UI(By.CSS_SELECTOR,
                               '*[id*="action_change_password"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'),
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'))
class UsersRow(ui.Row):
    pass


class UsersTable(ui.Table):
    columns = {'name': 2, 'email': 4}
    Row = UsersRow


@pom.register_ui(
    name_field=ui.TextField(By.NAME, 'name'),
    password_field=ui.TextField(By.NAME, 'password'),
    password_confirm_field=ui.TextField(By.NAME, 'confirm_password'),
    project_combobox=ui.ComboBox(By.NAME, 'project'))
class CreateUserForm(_ui.Form):
    pass


@pom.register_ui(
    password_field=ui.TextField(By.NAME, 'password'),
    confirm_password_field=ui.TextField(By.NAME, 'confirm_password'))
class ChangePasswordForm(_ui.Form):
    pass


@pom.register_ui(
    users_table=UsersTable(By.ID, 'users'),
    create_user_button=ui.Button(By.ID, 'users__action_create'),
    create_user_form=CreateUserForm(By.ID, 'create_user_form'),
    delete_users_button=ui.Button(By.ID, 'users__action_delete'),
    delete_user_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    change_password_form=ChangePasswordForm(By.ID,
                                            'change_user_password_form'))
class UsersPage(pom.Page):
    url = '/identity/users/'
