from selenium.webdriver.common.by import By

from horizon_autotests import pom
from horizon_autotests.pom import ui


class UsersTable(ui.Table):
    pass


class UsersPage(pom.Page):
    pass

UsersPage.register_ui(users_table=UsersTable(By.ID, 'users'))
