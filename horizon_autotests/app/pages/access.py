from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@ui.register_ui(field_name=ui.TextField(By.NAME, 'name'))
class FormCreateKeypair(_ui.Form):
    pass


@ui.register_ui(
    button_delete_keypair=ui.Button(By.CSS_SELECTOR, '[id*="action_delete"]'),
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'))
class RowKeypair(ui.Row):
    pass


class TableKeypairs(ui.Table):
    columns = {'name': 2}
    Row = RowKeypair


@ui.register_ui(field_name=ui.TextField(By.NAME, 'name'),
                field_public_key=ui.TextField(By.NAME, 'public_key'))
class FormImportKeypair(ui.Form):
    pass


@ui.register_ui(
    button_create_keypair=ui.Button(By.ID, 'keypairs__action_create'),
    button_delete_keypairs=ui.Button(By.ID, 'keypairs__action_delete'),
    button_import_keypair=ui.Button(By.ID, 'keypairs__action_import'),
    form_confirm_delete=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    form_create_keypair=FormCreateKeypair(By.ID, 'create_keypair_form'),
    form_import_keypair=FormImportKeypair(By.ID, 'import_keypair_form'),
    tab_keypairs=ui.UI(By.CSS_SELECTOR, '[data-target*="keypairs_tab"]'),
    table_keypairs=TableKeypairs(By.ID, 'keypairs'))
class AccessPage(BasePage):
    url = "/project/access_and_security/"
