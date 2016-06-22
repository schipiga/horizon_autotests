from .base import BasePage
from .login import LoginPage
from .users import UsersPage
from .volumes import VolumesPage
from .settings import SettingsPage
from .projects import ProjectsPage


pages = [
    LoginPage,
    VolumesPage,
    UsersPage,
    SettingsPage,
    ProjectsPage
]
