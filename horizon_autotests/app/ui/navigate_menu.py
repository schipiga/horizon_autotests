from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui
from horizon_autotests.pom.utils import Waiter

waiter = Waiter(polling=0.1)


class NavigateMenu(ui.Block):

    def go_to(self, item_names):
        container = self
        last_name = item_names[-1]
        is_expanded = lambda menu: 'in' in menu.webelement.get_attribute(
            'class').split()

        for item_name in item_names:
            item = ui.UI(
                By.XPATH, './li/a[contains(., "{}")]'.format(item_name))
            item.set_container(container)

            if item_name == last_name:
                item.click()
                break

            sub_menu = ui.Block(
                By.XPATH,
                ('./li/ul[contains(@class, "collapse") and preceding-sibling'
                 '::a[contains(., "{}")]]'.format(item_name)))
            sub_menu.set_container(container)

            if not is_expanded(sub_menu):
                item.click()

                if not waiter.exe(10, lambda: is_expanded(sub_menu)):
                    raise RuntimeError("Menu is not expanded after click")

            container = sub_menu
