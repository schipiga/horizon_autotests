from .base import BasePage
from .login import LoginPage
from .users import UsersPage
from .volumes import VolumesPage
from .settings import SettingsPage


pages = [
    LoginPage,
    VolumesPage,
    UsersPage,
    SettingsPage
]
