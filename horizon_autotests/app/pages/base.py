from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


@pom.register_ui(
    exit_item=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))
class AccountDropdown(ui.Block):
    pass


class ProjectDropdown(ui.Block):

    def project_item(self, name):
        selector = ('//ul[contains(@class, "dropdown-menu")]/li//span[contains'
                    '(@class, "dropdown-title") and contains(., "{}")]'.format(
                        name))
        item = ui.UI(By.XPATH, selector)
        item.set_container(self)
        return item


@pom.register_ui(close_button=ui.Button(By.CSS_SELECTOR, 'a.close'))
class Notification(ui.Block):
    levels = {'error': 'alert-danger',
              'info': 'alert-info',
              'success': 'alert-success'}


@pom.register_ui(
    account_dropdown=AccountDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'),
    project_dropdown=ProjectDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav > li.dropdown'),
    modal_spinner=ui.UI(By.CSS_SELECTOR, 'div.modal-dialog'))
class BasePage(pom.Page):
    url = '/'

    def notification(self, level):
        selector = 'div.alert.{}'.format(Notification.levels[level])
        _notification = Notification(By.CSS_SELECTOR, selector)
        _notification.set_container(self)
        return _notification
