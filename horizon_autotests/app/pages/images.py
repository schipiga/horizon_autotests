from pom import ui
from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui

from .base import BasePage


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_menu=_ui.DropdownMenu())
class RowImage(ui.Row):
    pass


class TableImages(ui.Table):
    columns = {'name': 2, 'type': 3, 'status': 4, 'format': 7}
    Row = RowImage


@ui.register_ui(
    table_images=TableImages(By.ID, 'images'))
class ImagesPage(BasePage):
    url = "/project/images/"
