from horizon_autotests.app.pages import UsersPage
from horizon_autotests.pom import ui

from .base import BaseSteps


class UsersSteps(BaseSteps):

    @property
    def users_page(self):
        if not isinstance(self.app.current_page, UsersPage):
            self.app.open(UsersPage)
        return self.app.current_page

    def create_user(self, username, password):
        self.users_page.create_user_button.click()
        with self.users_page.create_user_form as form:
            form.name_field.value = username
            form.password_field.value = password
            form.password_confirm_field.value = password
            form.submit()
        self.base_page.spinner.fade_out()

        row = self.users_page.users_table.row(name=username)
        assert ui.wait_for(10, lambda: row.is_present)

    def delete_user(self, username):
        row = self.users_page.users_table.row(name=username)
        row.dropdown_actions.toggle_button.click()
        row.dropdown_actions.delete_item.click()
        self.users_page.delete_user_confirm_form.submit()
        self.base_page.spinner.fade_out()

        assert ui.wait_for(10, lambda: not row.is_present)

    def delete_users(self, *usernames):
        rows = []
        for username in usernames:
            row = self.users_page.users_table.row(name=username)
            rows.append(row)
            row.checkbox.select()
        self.users_page.delete_users_button.click()
        self.users_page.delete_user_confirm_form.submit()
        self.base_page.spinner.fade_out()

        for row in rows:
            assert ui.wait_for(10, lambda: not row.is_present)
