from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


from .base import BasePage


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'))
class CreateKeypairForm(_ui.Form):
    pass


@pom.register_ui(
    delete_keypair_button=ui.Button(By.CSS_SELECTOR, '[id*="action_delete"]'),
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'))
class KeypairRow(ui.Row):
    pass


class KeypairsTable(ui.Table):
    columns = {'name': 2}
    Row = KeypairRow


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'),
                 public_key_field=ui.TextField(By.NAME, 'public_key'))
class ImportKeypairForm(ui.Form):
    pass


@pom.register_ui(
    keypairs_tab=ui.UI(By.CSS_SELECTOR, '[data-target*="keypairs_tab"]'),
    create_keypair_button=ui.Button(By.ID, 'keypairs__action_create'),
    create_keypair_form=CreateKeypairForm(By.ID, 'create_keypair_form'),
    keypairs_table=KeypairsTable(By.ID, 'keypairs'),
    import_keypair_button=ui.Button(By.ID, 'keypairs__action_import'),
    import_keypair_form=ImportKeypairForm(By.ID, 'import_keypair_form'),
    delete_keypairs_button=ui.Button(By.ID, 'keypairs__action_delete'),
    confirm_delete_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'))
class AccessPage(BasePage):
    url = "/project/access_and_security/"
