from pom import ui
from selenium.webdriver.common.by import By

from ..base import BasePage


@ui.register_ui(label_name=ui.UI(By.CSS_SELECTOR, 'dd:nth-of-type(1)'))
class Info(ui.Block):
    pass


@ui.register_ui(
    info_volume=Info(By.CSS_SELECTOR,
                     'div.detail dl.dl-horizontal:nth-of-type(1)'))
class VolumePage(BasePage):
    url = "/project/volumes/{}/"
