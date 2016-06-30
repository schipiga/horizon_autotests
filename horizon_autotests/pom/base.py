from selenium import webdriver

from .utils import cache

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

    @classmethod
    def register_ui(cls, **ui):
        for ui_name, ui_obj in ui.iteritems():

            def ui_getter(self, ui_obj=ui_obj):
                ui_clone = ui_obj.clone()
                ui_clone.set_container(self)
                return ui_clone

            ui_getter.__name__ = ui_name
            ui_getter = property(cache(ui_getter))
            setattr(cls, ui_name, ui_getter)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def find_element(self, locator):
        return self.webelement.find_element(*locator)

    def find_elements(self, locator):
        return self.webelement.find_elements(*locator)


class Page(Container):

    url = None

    def __init__(self, app):
        self.app = app
        self.webdriver = app.webdriver
        self.webelement = self.webdriver
