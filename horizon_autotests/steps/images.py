from horizon_autotests.app.pages import ImagesPage
from horizon_autotests.pom.utils import Waiter

from .base import BaseSteps

waiter = Waiter(polling=0.1)


class ImagesSteps(BaseSteps):

    @property
    def images_page(self):
        return self._open(ImagesPage)

    def delete_image(self, name):
        with self.images_page.images_table.row(name=name) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_item.click()
        self.images_page.delete_image_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence(30)
        self.close_notification('success')

        row.wait_for_absence(30)
