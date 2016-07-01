from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .tab_volumes import FormCreateSnapshot


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=_ui.DropdownMenu())
class RowSnapshot(ui.Row):
    pass


class TableSnapshots(_ui.Table):
    columns = {'name': 2,
               'description': 3,
               'size': 4,
               'status': 5,
               'volume_name': 6}
    Row = RowSnapshot


@ui.register_ui(
    button_delete_snapshots=ui.Button(By.ID,
                                      'volume_snapshots__action_delete'),
    form_edit_snapshot=FormCreateSnapshot(By.ID, 'update_snapshot_form'),
    table_snapshots=TableSnapshots(By.ID, 'volume_snapshots'))
class TabSnapshots(_ui.Tab):
    pass
