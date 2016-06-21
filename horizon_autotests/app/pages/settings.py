from selenium.webdriver.common import By
from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@pom.register_ui(lang_combobox=ui.ComboBox(By.NAME, 'language'),
                 timezone_combobox=ui.ComboBox(By.NAME, 'timezone'),
                 items_per_page_field=ui.TextField(By.NAME, 'pagesize'),
                 instance_log_length_field=ui.TextField(By.NAME,
                                                        'instance_log_length'))
class SettingsForm(_ui.Form):
    pass


@pom.register_ui(settings_form=SettingsForm(By.ID, 'user_settings_modal'))
class SettingsPage(BasePage):
    url = "/settings/"
