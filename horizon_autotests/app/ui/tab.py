from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui

from .initiated_ui import InitiatedUI


class Tab(ui.Block, InitiatedUI):

    def __init__(self, *args, **kwgs):
        self.locator = By.CSS_SELECTOR, 'body'
