class AuthSteps(object):

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.login_page.login_form.username.value = username
        self.login_page.login_form.password.value = password
        self.login_page.login_form.submit()
