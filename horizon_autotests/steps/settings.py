"""
Settings steps.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from horizon_autotests.app.pages import PageSettings

from .base import BaseSteps


class SettingsSteps(BaseSteps):
    """Settings steps."""

    def page_settings(self):
        """Open settings page if it isn't opened."""
        return self._open(PageSettings)

    def update_settings(self,
                        lang=None,
                        timezone=None,
                        items_per_page=None,
                        instance_log_length=None):
        """Step to update user settings."""
        with self.page_settings().form_settings as form:
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
        """Current user settings."""
        with self.page_settings().form_settings as form:
            return {
                'lang': form.combobox_lang.value,
                'timezone': form.combobox_timezone.value,
                'items_per_page': form.field_items_per_page.value,
                'instance_log_length': form.field_instance_log_length.value}
