from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@pom.register_ui(username=ui.TextField(By.NAME, 'username'),
                 password=ui.TextField(By.NAME, 'password'))
class LoginForm(_ui.Form):
    pass


@pom.register_ui(login_form=LoginForm(By.CSS_SELECTOR, 'form'))
class LoginPage(pom.Page):
    url = "/auth/login"
