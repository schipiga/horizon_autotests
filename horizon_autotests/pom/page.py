from .utils import Container


class Page(Container):

    url = None

    def __init__(self, app):
        self.app = app
        self.webdriver = app.webdriver
        self.webelement = self.webdriver
