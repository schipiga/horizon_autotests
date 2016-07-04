from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@ui.register_ui(button_close=ui.Button(By.CSS_SELECTOR, 'a.close'))
class Notification(ui.Block):
    levels = {'error': 'alert-danger',
              'info': 'alert-info',
              'success': 'alert-success'}


@ui.register_ui(navigate_menu=_ui.NavigateMenu(By.ID, 'sidebar-accordion'))
class BasePage(pom.Page, _ui.InitiatedUI):
    url = '/'
    navigate_item = None

    def notification(self, level):
        selector = 'div.alert.{}'.format(Notification.levels[level])
        _notification = Notification(By.CSS_SELECTOR, selector)
        _notification.set_container(self)
        return _notification

    def navigate(self, navigate_item):
        self.navigate_menu.go_to(navigate_item)
