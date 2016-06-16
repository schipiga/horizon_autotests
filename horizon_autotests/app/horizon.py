from horizon_autotests import pom


class Horizon(pom.App):

    current_page = None

    def __init__(self, url, *args, **kwgs):
        super(Horizon, self).__init__(url, 'firefox', *args, **kwgs)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(10)
        self.webdriver.set_page_load_timeout(30)
        self.webdriver.get(url)

    def open(self, page):
        if issubclass(page, pom.Page):
            url = page.url
            self.current_page = page(self)
        else:
            url = page
            self.current_page = None
        super(Horizon, self).open(url)
