from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@ui.register_ui(dropdown_menu=_ui.DropdownMenu())
class SnapshotRow(ui.Row):
    pass


class SnapshotsTable(ui.Table):
    columns = {'name': 2,
               'description': 3,
               'size': 4,
               'status': 5,
               'volume_name': 6}
    Row = SnapshotRow


@ui.register_ui(
    snapshots_table=SnapshotsTable(By.ID, 'volume_snapshots'))
class TabSnapshots(_ui.Tab):
    pass
