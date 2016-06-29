from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'))
class ImageRow(ui.Row):
    pass


class ImagesTable(ui.Table):
    columns = {'name': 2, 'type': 3, 'status': 4, 'format': 7}
    Row = ImageRow


@pom.register_ui(
    images_table=ImagesTable(By.ID, 'images'),
    delete_image_confirm_form=_ui.Form(By.CSS_SELECTOR, 'div.modal-content'))
class ImagesPage(BasePage):
    url = "/project/images/"
