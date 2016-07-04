import pom

from .pages import pages


class Horizon(pom.App):

    def __init__(self, url, *args, **kwgs):
        super(Horizon, self).__init__(url, 'firefox', *args, **kwgs)
        self.webdriver.maximize_window()
        self.webdriver.set_window_size(1920, 1080)
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
        current_url = self.webdriver.current_url
        for page in pages:
            url = self.app_url + page.url

            if current_url.startswith(url):
                url_end = current_url.split(url)[-1]

                if not (url_end and url_end[0].isalnum()):
                    return page(self)
