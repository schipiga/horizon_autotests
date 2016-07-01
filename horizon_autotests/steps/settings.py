from horizon_autotests.app.pages import SettingsPage

from .base import BaseSteps


class SettingsSteps(BaseSteps):

    @property
    def settings_page(self):
        return self._open(SettingsPage)

    def update_settings(self, lang=None, timezone=None, items_per_page=None,
                        instance_log_length=None):
        with self.settings_page.form_settings as form:
            if lang:
                form.combobox_lang.value = lang
            if timezone:
                form.combobox_timezone.value = timezone
            if items_per_page:
                form.field_items_per_page.value = items_per_page
            if instance_log_length:
                form.field_instance_log_length.value = instance_log_length
            form.submit()
        self.close_notification('success')

    @property
    def current_settings(self):
        with self.settings_page.form_settings as form:
            return {
                'lang': form.combobox_lang.value,
                'timezone': form.combobox_timezone.value,
                'items_per_page': form.field_items_per_page.value,
                'instance_log_length': form.field_instance_log_length.value}
