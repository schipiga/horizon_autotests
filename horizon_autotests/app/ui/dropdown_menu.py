from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui


@ui.register_ui(
    button_toggle=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    item_default=ui.UI(By.CSS_SELECTOR, 'a:nth-of-type(1)'),
    item_delete=ui.UI(By.CSS_SELECTOR, '[id$="action_delete"]'),
    item_edit=ui.UI(By.CSS_SELECTOR, '[id$="action_edit"]'))
class DropdownMenu(ui.Block):

    def __init__(self, *args, **kwgs):
        self.locator = By.CSS_SELECTOR, 'div.btn-group'
