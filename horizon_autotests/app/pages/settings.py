from pom import ui
from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui

from .base import BasePage


@ui.register_ui(
    combobox_lang=ui.ComboBox(By.NAME, 'language'),
    combobox_timezone=ui.ComboBox(By.NAME, 'timezone'),
    field_items_per_page=ui.IntegerField(By.NAME, 'pagesize'),
    field_instance_log_length=ui.IntegerField(By.NAME, 'instance_log_length'))
class FormSettings(_ui.Form):
    pass


@ui.register_ui(form_settings=FormSettings(By.ID, 'user_settings_modal'))
class SettingsPage(BasePage):
    url = "/settings/"
