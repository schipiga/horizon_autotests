from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


ERROR = 'alert-danger'
INFO = 'alert-info'
SUCCESS = 'alert-success'


@pom.register_ui(
    exit_item=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))
class AccountDropdown(ui.Block):
    pass


@pom.register_ui(close_button=ui.Button(By.CSS_SELECTOR, 'a.close'))
class Notification(ui.Block):

    def level(self, level):
        by, selector = self.locator
        selector = selector.format(level)
        self.locator = by, selector
        return self


@pom.register_ui(
    account_dropdown=AccountDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'),
    modal_spinner=ui.UI(By.CSS_SELECTOR, 'div.modal-dialog'),
    notification=Notification(By.CSS_SELECTOR, 'div.alert.{}'))
class BasePage(pom.Page):
    url = '/'
