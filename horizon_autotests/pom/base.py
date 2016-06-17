from selenium import webdriver

__all__ = [
    'App',
    'Page',
    'register_ui'
]


browsers = {
    'firefox': webdriver.Firefox,
    'phantom': webdriver.PhantomJS,
    'Chrome': webdriver.Chrome,
}


class App(object):

    def __init__(self, url, browser, *args, **kwgs):
        self.app_url = url.strip('/')
        self.webdriver = browsers[browser](*args, **kwgs)

    def open(self, url):
        self.webdriver.get(self.app_url + url)

    def quit(self):
        self.webdriver.quit()


def register_ui(**ui):

    def wrapper(cls):
        cls.register_ui(**ui)
        return cls

    return wrapper


class Container(object):

    _registered_ui = None

    @classmethod
    def register_ui(cls, **ui):
        if not cls._registered_ui:
            cls._registered_ui = {}
        cls._registered_ui.update(ui)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def find_element(self, locator):
        return self.webelement.find_element(*locator)

    def find_elements(self, locator):
        return self.webelement.find_elements(*locator)

    def __getattr__(self, name):
        ui_obj = self._registered_ui.get(name)
        if not ui_obj:
            raise AttributeError("Attribute {!r} isn't defined".format(name))
        ui_obj.set_container(self)
        return ui_obj


class Page(Container):

    url = None

    def __init__(self, app):
        self.app = app
        self.webdriver = app.webdriver
        self.webelement = self.webdriver
