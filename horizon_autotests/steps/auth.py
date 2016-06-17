from horizon_autotests.app.pages import LoginPage

from .base import BaseSteps


class AuthSteps(BaseSteps):

    @property
    def login_page(self):
        if not isinstance(self.app.current_page, LoginPage):
            self.app.open(LoginPage)
        return LoginPage(self.app)

    def login(self, username, password):
        with self.login_page.login_form as form:
            form.username.value = username
            form.password.value = password
            form.submit()

    def logout(self):
        self.base_page.account_dropdown.click()
        self.base_page.account_dropdown.exit_item.click()
