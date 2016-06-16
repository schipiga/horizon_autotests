def test_login(auth_steps):
    auth_steps.login('admin', 'admin')
    auth_steps.logout()
