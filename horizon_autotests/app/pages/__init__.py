from .access import AccessPage
from .base import BasePage
from .instances import InstancesPage
from .login import LoginPage
from .projects import ProjectsPage
from .settings import SettingsPage
from .users import UsersPage
from .volumes import AdminVolumesPage, VolumesPage

pages = [
    AccessPage,
    AdminVolumesPage,
    InstancesPage,
    LoginPage,
    ProjectsPage,
    SettingsPage,
    UsersPage,
    VolumesPage
]
