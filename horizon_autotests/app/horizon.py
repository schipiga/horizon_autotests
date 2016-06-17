from horizon_autotests import pom

from .pages import pages


class Horizon(pom.App):

    def __init__(self, url, *args, **kwgs):
        super(Horizon, self).__init__(url, 'firefox', *args, **kwgs)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(5)
        self.webdriver.set_page_load_timeout(30)
        self.webdriver.get(self.app_url)

    def open(self, page):
        if issubclass(page, pom.Page):
            url = page.url
        else:
            url = page
        super(Horizon, self).open(url)

    @property
    def current_page(self):
        for page in pages:
            if self.webdriver.current_url.startswith(self.app_url + page.url):
                return page(self)
