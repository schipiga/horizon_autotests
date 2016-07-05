from pom import ui
from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui


@ui.register_ui(
    item_update_volume_status=ui.UI(
        By.CSS_SELECTOR, '*[id*="action_update_status"]'))
class DropdownMenu(_ui.DropdownMenu):
    pass


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=DropdownMenu())
class RowVolume(ui.Row):
    pass


class TableVolumes(ui.Table):
    columns = {'name': 4, 'size': 5, 'status': 6, 'type': 7}
    Row = RowVolume


@ui.register_ui(status_combobox=ui.ComboBox(By.NAME, 'status'))
class UpdateVolumeStatusForm(_ui.Form):
    pass


@ui.register_ui(
    table_volumes=TableVolumes(By.CSS_SELECTOR, 'table[id="volumes"]'),
    form_update_volume_status=UpdateVolumeStatusForm(
        By.CSS_SELECTOR, 'form[action*="/update_status"]'))
class TabAdminVolumes(_ui.Tab):
    pass
