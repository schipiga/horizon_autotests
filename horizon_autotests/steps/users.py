from horizon_autotests.app.pages import UsersPage
from horizon_autotests.pom.utils import Waiter
from .base import BaseSteps

waiter = Waiter(polling=0.1)


class UsersSteps(BaseSteps):

    @property
    def users_page(self):
        return self._open(UsersPage)

    def create_user(self, username, password, project=None):
        self.users_page.create_user_button.click()
        with self.users_page.create_user_form as form:
            form.name_field.value = username
            form.password_field.value = password
            form.password_confirm_field.value = password
            if project:
                form.project_combobox.value = project
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        row = self.users_page.users_table.row(name=username)
        assert waiter.exe(10, lambda: row.is_present)

    def delete_user(self, username):
        with self.users_page.users_table.row(name=username) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.delete_item.click()
        self.users_page.delete_user_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        assert waiter.exe(10, lambda: not row.is_present)

    def delete_users(self, *usernames):
        rows = []
        for username in usernames:
            row = self.users_page.users_table.row(name=username)
            rows.append(row)
            row.checkbox.select()
        self.users_page.delete_users_button.click()
        self.users_page.delete_user_confirm_form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')

        for row in rows:
            assert waiter.exe(10, lambda: not row.is_present)

    def change_user_password(self, username, new_password):
        with self.users_page.users_table.row(name=username) as row:
            row.dropdown_actions.toggle_button.click()
            row.dropdown_actions.change_password_item.click()
        with self.users_page.change_password_form as form:
            form.password_field.value = new_password
            form.confirm_password_field.value = new_password
            form.submit()
        self.base_page.modal_spinner.wait_for_absence()
        self.close_notification('success')
