from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@ui.register_ui(
    field_description=ui.TextField(By.NAME, 'vol_type_description'),
    field_name=ui.TextField(By.NAME, 'name'))
class FormCreateVolumeType(_ui.Form):
    pass


@ui.register_ui(dropdown_menu=_ui.DropdownMenu())
class RowVolumeType(ui.Row):
    pass


class TableVolumeTypes(ui.Table):
    columns = {'name': 2}
    Row = RowVolumeType


@ui.register_ui(dropdown_menu=_ui.DropdownMenu())
class RowQosSpec(ui.Row):
    pass


class TableQosSpecs(ui.Table):
    columns = {'name': 2}
    Row = RowQosSpec


@ui.register_ui(
    field_consumer=ui.ComboBox(By.NAME, 'consumer'),
    field_name=ui.TextField(By.NAME, 'name'))
class FormCreateQosSpec(_ui.Form):
    pass


@ui.register_ui(
    button_create_qos_spec=ui.Button(By.ID, 'qos_specs__action_create'),
    button_create_volume_type=ui.Button(By.ID, 'volume_types__action_create'),
    form_create_qos_spec=FormCreateQosSpec(
        By.CSS_SELECTOR, 'form[action*="volume_types/create_qos_spec"]'),
    form_create_volume_type=FormCreateVolumeType(
        By.CSS_SELECTOR, 'form[action*="volume_types/create_type"]'),
    table_qos_specs=TableQosSpecs(By.ID, 'qos_specs'),
    table_volume_types=TableVolumeTypes(By.ID, 'volume_types'))
class TabVolumeTypes(_ui.Tab):
    pass
