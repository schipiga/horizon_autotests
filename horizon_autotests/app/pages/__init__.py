from .access import AccessPage
from .base import BasePage  # noqa
from .images import ImagesPage
from .instances import InstancesPage
from .login import LoginPage
from .projects import ProjectsPage
from .settings import SettingsPage
from .users import UsersPage
from .volumes import AdminVolumesPage, VolumePage, VolumesPage

pages = [
    AccessPage,
    AdminVolumesPage,
    ImagesPage,
    InstancesPage,
    LoginPage,
    ProjectsPage,
    SettingsPage,
    UsersPage,
    VolumePage,
    VolumesPage
]
