from selenium.webdriver import ActionChains
from horizon_autotests.pom.utils import Container


class UI(object):

    container = None

    def __init__(self, *locator):
        self.locator = locator

    def set_container(self, container):
        self.container = container

    def click(self):
        self.webelement.click()

    def right_click(self):
        self._action_chains.context_click(self.webelement).perform()

    def double_click(self):
        self._action_chains.double_click(self.webelement).perform()

    @property
    def is_present(self):
        try:
            self.webelement.is_displayed()
            return True
        except Exception:
            return False

    @property
    def is_enabled(self):
        return self.webelement.is_enabled()

    @property
    def is_visible(self):
        return self.webelement.is_displayed()

    @property
    def web_driver(self):
        return self.container.web_driver

    @property
    def webelement(self):
        return self.container.find_element(self.locator)

    @property
    def _action_chains(self):
        return ActionChains(self.web_driver)

    def clone(self):
        return self.__class__(*self.locator)


class Block(UI, Container):
    pass
