from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from ..instances import FormLaunchInstance


@ui.register_ui(
    field_name_=ui.TextField(By.NAME, 'name'),
    combobox_image_source=ui.ComboBox(By.NAME, 'image_source'),
    combobox_source_type=ui.ComboBox(By.NAME, 'volume_source_type'),
    combobox_volume_type=ui.ComboBox(By.NAME, 'type'))
class FormCreateVolume(_ui.Form):
    pass


@ui.register_ui(field_name=ui.TextField(By.NAME, 'name'))
class FormEditVolume(_ui.Form):
    pass


@ui.register_ui(
    item_change_volume_type=ui.UI(By.CSS_SELECTOR, '*[id$="action_retype"]'),
    item_create_snapshot=ui.UI(By.CSS_SELECTOR, 'a[id$="action_snapshots"]'),
    item_extend_volume=ui.UI(By.CSS_SELECTOR, '*[id$="action_extend"]'),
    item_launch_volume_as_instance=ui.UI(By.CSS_SELECTOR,
                                         '*[id$="action_launch_volume_ng"]'),
    item_upload_to_image=ui.UI(By.CSS_SELECTOR,
                               '*[id$="action_upload_to_image"]'))
class DropdownMenu(_ui.DropdownMenu):
    pass


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=DropdownMenu(),
    link_volume=ui.UI(By.CSS_SELECTOR, 'td > a'))
class RowVolume(ui.Row):
    pass


class TableVolume(_ui.Table):
    columns = {'name': 2, 'size': 4, 'status': 5, 'type': 6}
    Row = RowVolume


@ui.register_ui(combobox_volume_type=ui.ComboBox(By.NAME, 'volume_type'))
class FormChangeVolumeType(_ui.Form):
    pass


@ui.register_ui(field_image_name=ui.TextField(By.NAME, 'image_name'))
class FormUploadToImage(_ui.Form):
    pass


@ui.register_ui(field_new_size=ui.IntegerField(By.NAME, 'new_size'))
class FormExtendVolume(_ui.Form):
    pass


@ui.register_ui(
    button_create_volume=ui.Button(By.ID, 'volumes__action_create'),
    button_delete_volumes=ui.Button(By.ID, 'volumes__action_delete'),
    form_change_volume_type=FormChangeVolumeType(By.CSS_SELECTOR,
                                                 'form[action*="/retype"]'),
    form_create_volume=FormCreateVolume(By.CSS_SELECTOR,
                                        'form[action*="volumes/create"]'),
    form_extend_volume=FormExtendVolume(By.CSS_SELECTOR,
                                        'form[action*="/extend"]'),
    form_launch_instance=FormLaunchInstance(
        By.CSS_SELECTOR,
        'wizard[ng-controller="LaunchInstanceWizardController"]'),
    form_upload_to_image=FormUploadToImage(By.CSS_SELECTOR,
                                           'form[action*="/upload_to_image"]'),
    table_volumes=TableVolume(By.ID, 'volumes'))
class TabVolumes(_ui.Tab):
    pass
