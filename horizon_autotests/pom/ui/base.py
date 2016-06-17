import time
from selenium.webdriver import ActionChains
from horizon_autotests.pom.utils import Container


def wait_for(timeout, func, *args, **kwgs):
    if not timeout:
        return func(*args, **kwgs) or False
    limit = int(time.time()) + timeout
    while int(time.time()) <= limit:
        result = func(*args, **kwgs)
        if result:
            return result
        time.sleep(0.1)
    return False


def wait_for_visibility(func):

    def wrapper(self, *args, **kwgs):
        if not self.webelement.is_displayed():
            if not wait_for(5, lambda: self.is_visible):
                raise Exception("{} is not visible", self.locator)
        return func(self, *args, **kwgs)

    return wrapper


def immediately(func):

    def wrapper(self, *args, **kwgs):
        try:
            self.webdriver.implicitly_wait(0)
            return func(self, *args, **kwgs)
        finally:
            self.webdriver.implicitly_wait(5)

    return wrapper


class UI(object):

    container = None

    def __init__(self, *locator):
        self.locator = locator

    def set_container(self, container):
        self.container = container

    @wait_for_visibility
    def click(self):
        self.webelement.click()

    @wait_for_visibility
    def right_click(self):
        self._action_chains.context_click(self.webelement).perform()

    @wait_for_visibility
    def double_click(self):
        self._action_chains.double_click(self.webelement).perform()

    @property
    @immediately
    def is_present(self):
        try:
            self.webelement.is_displayed()
            return True
        except Exception:
            return False

    @property
    @immediately
    def is_enabled(self):
        return self.webelement.is_enabled()

    @property
    @immediately
    def is_visible(self):
        return self.webelement.is_displayed()

    @property
    def webdriver(self):
        return self.container.webdriver

    @property
    def webelement(self):
        return self.container.find_element(self.locator)

    @property
    def _action_chains(self):
        return ActionChains(self.webdriver)

    def clone(self):
        return self.__class__(*self.locator)


class Block(UI, Container):
    pass
