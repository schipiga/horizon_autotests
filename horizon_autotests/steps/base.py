from horizon_autotests.app.pages import BasePage


class BaseSteps(object):

    def __init__(self, app):
        self.app = app

    @property
    def base_page(self):
        return BasePage(self.app)

    def _open(self, page):
        if not isinstance(self.app.current_page, page):
            self.app.open(page)
        return page(self.app)
