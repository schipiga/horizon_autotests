from horizon_autotests.app.pages import LoginPage, BasePage


class AuthSteps(object):

    def __init__(self, app):
        self.app = app

    @property
    def login_page(self):
        if not isinstance(self.app.current_page, LoginPage):
            self.app.open(LoginPage)
        return self.app.current_page

    @property
    def base_page(self):
        return BasePage(self.app)

    def login(self, username, password):
        self.login_page.login_form.username.value = username
        self.login_page.login_form.password.value = password
        self.login_page.login_form.submit()

    def logout(self):
        self.base_page.account_dropdown.click()
        self.base_page.account_dropdown.exit_item.click()
