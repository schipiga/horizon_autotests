from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class AccountDropdown(ui.Block):
    pass

AccountDropdown.register_ui(
    exit_item=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))


class Spinner(ui.UI):

    def fade_out(self):
        if not ui.wait_for(30, lambda: not self.is_present):
            raise Exception('Spinner still present')


class BasePage(pom.Page):
    url = '/'

BasePage.register_ui(
    account_dropdown=AccountDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'),
    spinner=Spinner(By.CSS_SELECTOR, 'div.modal-dialog'))
