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


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'))
class EditVolumeForm(_ui.Form):
    pass


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'),
    edit_volume_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_edit"]'))
class VolumesRow(ui.Row):
    pass


class VolumesTable(ui.Table):
    columns = {'name': 2, 'status': 5}
    Row = VolumesRow


@pom.register_ui(
    create_volume_button=ui.Button(By.ID, 'volumes__action_create'),
    delete_volumes_button=ui.Button(By.ID, 'volumes__action_delete'),
    create_volume_form=CreateVolumeForm(By.CSS_SELECTOR,
                                        'form[action*="volumes/create"]'),
    delete_volume_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    volumes_table=VolumesTable(By.ID, 'volumes'),
    edit_volume_form=EditVolumeForm(By.CSS_SELECTOR, 'form[action*="update"]'))
class VolumesPage(pom.Page):
    url = "/project/volumes/"


@pom.register_ui(
    name_field=ui.TextField(By.NAME, 'name'),
    description_field=ui.TextField(By.NAME, 'vol_type_description'))
class CreateVolumeTypeForm(_ui.Form):
    pass


@pom.register_ui(
    create_encryption_item=ui.UI(By.CSS_SELECTOR,
                                 '*[id*="create_encryption"]'),
    toggle_button=ui.Button(By.CSS_SELECTOR, '.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    dropdown_actions=DropdownActions(By.CSS_SELECTOR,
                                     'td.actions_column div.btn-group'))
class VolumeTypesRow(ui.Row):
    pass


class VolumeTypesTable(ui.Table):
    columns = {'name': 2}
    Row = VolumeTypesRow


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, '.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(dropdown_actions=DropdownActions(
    By.CSS_SELECTOR, 'td.actions_column div.btn-group'))
class QosSpecRow(ui.Row):
    pass


class QosSpecsTable(ui.Table):
    columns = {'name': 2}
    Row = QosSpecRow


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'),
                 consumer_field=ui.ComboBox(By.NAME, 'consumer'))
class CreateQosSpecForm(_ui.Form):
    pass


@pom.register_ui(
    volume_types_tab=ui.UI(By.CSS_SELECTOR,
                           'a[data-target*="volume_types_tab"]'),
    create_volume_type_button=ui.Button(By.ID, 'volume_types__action_create'),
    create_volume_type_form=CreateVolumeTypeForm(
        By.CSS_SELECTOR, 'form[action*="volume_types/create_type"]'),
    volume_types_table=VolumeTypesTable(By.ID, 'volume_types'),
    confirm_delete_volume_types_form=_ui.Form(By.CSS_SELECTOR,
                                              'div.modal-content'),
    create_qos_spec_button=ui.Button(By.ID, 'qos_specs__action_create'),
    create_qos_spec_form=CreateQosSpecForm(
        By.CSS_SELECTOR, 'form[action*="volume_types/create_qos_spec"]'),
    qos_specs_table=QosSpecsTable(By.ID, 'qos_specs'),
    confirm_delete_qos_specs_form=_ui.Form(By.CSS_SELECTOR,
                                           'div.modal-content'))
class AdminVolumesPage(pom.Page):
    url = "/admin/volumes/"
