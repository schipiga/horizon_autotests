from horizon_autotests.app.pages import VolumesPage
from horizon_autotests.app.pages.base import ERROR, INFO, SUCCESS

from .base import BaseSteps


class VolumesSteps(BaseSteps):

    @property
    def volumes_page(self):
        if not isinstance(self.app.current_page, VolumesPage):
            self.app.open(VolumesPage)
        return VolumesPage(self.app)

    def create_volume(self, name, source_type='Image'):
        self.volumes_page.create_volume_button.click()
        with self.volumes_page.create_volume_form as form:
            form.name_field.value = name
            form.source_type_combobox.value = source_type
            image_sources = form.image_source_combobox.values
            form.image_source_combobox.value = image_sources[-1]
            volume_types = form.volume_type_combobox.values
            form.volume_type_combobox.value = volume_types[-1]
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.base_page.notification.level(INFO).close_button.click()
