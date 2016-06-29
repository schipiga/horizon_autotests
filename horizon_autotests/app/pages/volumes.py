from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .instances import LaunchInstanceForm


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
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'),
    change_volume_type_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_retype"]'),
    upload_to_image_item=ui.UI(By.CSS_SELECTOR,
                               '*[id*="action_upload_to_image"]'),
    extend_volume_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_extend"]'),
    launch_volume_as_instance_item=ui.UI(By.CSS_SELECTOR,
                                         '*[id*="action_launch_volume_ng"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'),
    edit_volume_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_edit"]'),
    volume_link=ui.UI(By.CSS_SELECTOR, 'a'))
class VolumesRow(ui.Row):
    pass


class VolumesTable(ui.Table):
    columns = {'name': 2, 'size': 4, 'status': 5, 'type': 6}
    Row = VolumesRow


@pom.register_ui(volume_type_combobox=ui.ComboBox(By.NAME, 'volume_type'))
class ChangeVolumeTypeForm(_ui.Form):
    pass


@pom.register_ui(image_name_field=ui.TextField(By.NAME, 'image_name'))
class UploadToImageForm(_ui.Form):
    pass


@pom.register_ui(new_size_field=ui.IntegerField(By.NAME, 'new_size'))
class ExtendVolumeForm(_ui.Form):
    pass


@pom.register_ui(
    create_volume_button=ui.Button(By.ID, 'volumes__action_create'),
    delete_volumes_button=ui.Button(By.ID, 'volumes__action_delete'),
    create_volume_form=CreateVolumeForm(By.CSS_SELECTOR,
                                        'form[action*="volumes/create"]'),
    delete_volume_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'),
    volumes_table=VolumesTable(By.ID, 'volumes'),
    edit_volume_form=EditVolumeForm(By.CSS_SELECTOR, 'form[action*="update"]'),
    next_link=ui.UI(By.CSS_SELECTOR, 'a[href^="?marker="]'),
    prev_link=ui.UI(By.CSS_SELECTOR, 'a[href^="?prev_marker="]'),
    change_volume_type_form=ChangeVolumeTypeForm(By.CSS_SELECTOR,
                                                 'form[action*="/retype"]'),
    upload_to_image_form=UploadToImageForm(By.CSS_SELECTOR,
                                           'form[action*="/upload_to_image"]'),
    extend_volume_form=ExtendVolumeForm(By.CSS_SELECTOR,
                                        'form[action*="/extend"]'),
    launch_instance_form=LaunchInstanceForm(
        By.CSS_SELECTOR,
        'wizard[ng-controller="LaunchInstanceWizardController"]'))
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
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    update_volume_status_item=ui.UI(By.CSS_SELECTOR,
                                    '*[id*="action_update_status"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'))
class AdminVolumeRow(ui.Row):
    pass


class AdminVolumesTable(ui.Table):
    columns = {'name': 4, 'size': 5, 'status': 6, 'type': 7}
    Row = AdminVolumeRow


@pom.register_ui(status_combobox=ui.ComboBox(By.NAME, 'status'))
class UpdateVolumeStatusForm(_ui.Form):
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
                                           'div.modal-content'),
    volumes_table=AdminVolumesTable(By.CSS_SELECTOR, 'table[id="volumes"]'),
    update_volume_status_form=UpdateVolumeStatusForm(
        By.CSS_SELECTOR, 'form[action*="/update_status"]'))
class AdminVolumesPage(pom.Page):
    url = "/admin/volumes/"


@pom.register_ui(name_label=ui.UI(By.CSS_SELECTOR, 'dd:nth-of-type(1)'))
class Info(ui.Block):
    pass


@pom.register_ui(
    volume_info=Info(By.CSS_SELECTOR,
                     'div.detail dl.dl-horizontal:nth-of-type(1)'))
class VolumePage(pom.Page):
    url = "/project/volumes/{}/"
