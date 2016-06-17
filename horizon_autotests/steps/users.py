from .base import BaseSteps


class UsersSteps(BaseSteps):

    def create_user(self, username, password):
        self.users_page.create_user_button.click()
        self.users_page.create_user_form.name_field.value = username
        self.users_page.create_user_form.password_field.value = password
        self.users_page.create_user_form.password_confirm_field.value = password
        self.users_page.create_user_form.submit()

    def delete_user(self, username):
        row = self.users_page.users_table.row(name=username)
        row.actions_dropdown.click()
        row.actions_dropdown.delete_item.click()
        self.users_page.delete_user_confirm_form.click()
