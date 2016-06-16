from selenium.webdriver import ActionChains


class UI(object):

    container = None

    def __init__(self, *locator):
        self.locator = locator

    def set_container(self, container):
        self.container = container

    def click(self):
        self.web_element.click()

    def right_click(self):
        self._action_chains.context_click(self.web_element).perform()

    def double_click(self):
        self._action_chains.double_click(self.web_element).perform()

    @property
    def is_present(self):
        try:
            self.web_element.is_displayed()
            return True
        except Exception:
            return False

    @property
    def is_enabled(self):
        return self.web_element.is_enabled()

    @property
    def is_visible(self):
        return self.web_element.is_displayed()

    @property
    def web_driver(self):
        return self.container.web_driver

    @property
    def web_element(self):
        self.container.find_element(self.locator)

    @property
    def _action_chains(self):
        return ActionChains(self.web_driver)

    def clone(self, locator=None, container=None):
        return type(self)(locator or self.locator, container or self.container)
