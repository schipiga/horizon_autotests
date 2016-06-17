from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@pom.register_ui(
    name_field=ui.TextField(By.NAME, 'name'),
    source_type_combobox=ui.ComboBox(By.NAME, 'volume_source_type'),
    image_source_combobox=ui.ComboBox(By.NAME, 'image_source'),
    volume_type_combobox=ui.ComboBox(By.NAME, 'type'))
class CreateVolumeForm(_ui.Form):
    pass


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'))
class VolumesRow(ui.Row):
    pass


class VolumesTable(ui.Table):
    columns = {'name': 2, 'status': 5}
    Row = VolumesRow


@pom.register_ui(
    create_volume_button=ui.Button(By.ID, 'volumes__action_create'),
    create_volume_form=CreateVolumeForm(By.CSS_SELECTOR,
                                        'form[action*="volumes/create"]'),
    delete_volume_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    volumes_table=VolumesTable(By.ID, 'volumes'))
class VolumesPage(pom.Page):
    url = "/project/volumes/"
