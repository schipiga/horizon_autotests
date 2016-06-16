from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class AccountDropdown(ui.Block):
    pass

AccountDropdown.register_ui(
    exit_item=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))


class BasePage(pom.Page):
    url = '/'

BasePage.register_ui(
    account_dropdown=AccountDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'))
