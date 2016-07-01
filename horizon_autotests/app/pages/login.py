from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui


@ui.register_ui(field_username=ui.TextField(By.NAME, 'username'),
                field_password=ui.TextField(By.NAME, 'password'))
class FormLogin(_ui.Form):
    pass


@ui.register_ui(form_login=FormLogin(By.CSS_SELECTOR, 'form'))
class LoginPage(pom.Page):
    url = "/auth/login"
