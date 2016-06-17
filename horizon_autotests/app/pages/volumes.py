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
    create_volume_button=ui.Button(By.ID, 'volumes__action_create'),
    create_volume_form=CreateVolumeForm(By.CSS_SELECTOR,
                                        'form[action*="volumes/create"]'))
class VolumesPage(pom.Page):
    url = "/project/volumes/"
