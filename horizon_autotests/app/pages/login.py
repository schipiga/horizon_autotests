from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class LoginForm(pom.ui.Form):
    pass

LoginForm.register_ui(
    username_field=ui.TextField(By.CSS_SELECTOR, 'input[name="username"]'),
    password_field=ui.TextField(By.CSS_SELECTOR, 'input[name="password"]'))


class LoginPage(pom.Page):
    url = "/login"

LoginPage.register_ui(login_form=LoginForm(By.CSS_SELECTOR, 'div.form'))
