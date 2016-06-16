from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class LoginForm(pom.ui.Form):
    pass

LoginForm.register_ui(username=ui.TextField(By.NAME, 'username'),
                      password=ui.TextField(By.NAME, 'password'))


class LoginPage(pom.Page):
    url = "/auth/login"

LoginPage.register_ui(login_form=LoginForm(By.CSS_SELECTOR, 'form'))
