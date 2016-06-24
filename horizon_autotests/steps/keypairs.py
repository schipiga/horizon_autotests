from horizon_autotests.app.pages import AccessPage

from .base import BaseSteps


class KeypairsSteps(BaseSteps):

    def keypairs_page(self):
        access_page = self._open(AccessPage)
        access_page.keypairs_tab.click()
        return access_page

    def create_keypair(self, name):
        page = self.keypairs_page()
        page.create_keypair_button.click()

        with page.create_keypair_form as form:
            form.name_field.value = name
            form.submit()

        self.base_page.modal_spinner.wait_for_absence()

        self.keypairs_page().keypairs_table.row(name=name).wait_for_presence()

    def delete_keypair(self, name):
        page = self.keypairs_page()
        page.keypairs_table.row(name=name).delete_keypair_button.click()
        page.confirm_delete_form.submit()

        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        page.keypairs_table.row(name=name).wait_for_absence()

    def import_keypair(self, name, public_key):
        page = self.keypairs_page()
        page.import_keypair_button.click()

        with page.import_keypair_form as form:
            form.name_field.value = name
            form.public_key_field.value = public_key
            form.submit()

        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        page.keypairs_table.row(name=name).wait_for_presence()

    def delete_keypairs(self, *names):
        page = self.keypairs_page()

        for name in names:
            page.keypairs_table.row(name=name).checkbox.select()

        page.delete_keypairs_button.click()
        page.confirm_delete_form.submit()

        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        page.keypairs_table.row(name=name).wait_for_absence()
