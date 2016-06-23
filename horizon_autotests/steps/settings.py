from horizon_autotests.app.pages import SettingsPage

from .base import BaseSteps


class SettingsSteps(BaseSteps):

    @property
    def settings_page(self):
        return self._open(SettingsPage)

    def update_settings(self, lang=None, timezone=None, items_per_page=None,
                        instance_log_length=None):
        with self.settings_page.settings_form as form:
            if lang:
                form.lang_combobox.value = lang
            if timezone:
                form.timezone_combobox.value = timezone
            if items_per_page:
                form.items_per_page_field.value = items_per_page
            if instance_log_length:
                form.instance_log_length_field.value = instance_log_length
            form.submit()
        self.close_notification('success')

    @property
    def current_settings(self):
        with self.settings_page.settings_form as form:
            return {
                'lang': form.lang_combobox.value,
                'timezone': form.timezone_combobox.value,
                'items_per_page': form.items_per_page_field.value,
                'instance_log_length': form.instance_log_length_field.value}
