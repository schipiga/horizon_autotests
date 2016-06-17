from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class DropdownActions(ui.Block):
    pass

DropdownActions.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, 'button[id*="action_delete"]'))


class UsersRow(ui.Row):
    pass

UsersRow.register_ui(
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'))


class UsersTable(ui.Table):
    columns = {'name': 2, 'email': 4}
    Row = UsersRow


class CreateUserForm(ui.Form):
    pass

CreateUserForm.register_ui(
    name_field=ui.TextField(By.NAME, 'name'),
    password_field=ui.TextField(By.NAME, 'password'),
    password_confirm_field=ui.TextField(By.NAME, 'confirm_password'))


class UsersPage(pom.Page):
    url = '/identity/users/'

UsersPage.register_ui(
    users_table=UsersTable(By.ID, 'users'),
    create_user_button=ui.Button(By.ID, 'users__action_create'),
    create_user_form=CreateUserForm(By.ID, 'create_user_form'),
    delete_user_confirm_form=ui.Form(By.CSS_SELECTOR, 'div.modal-content'))
