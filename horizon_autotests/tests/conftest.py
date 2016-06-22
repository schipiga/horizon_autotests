import os

import pytest
import attrdict

from horizon_autotests.app import Horizon
from horizon_autotests.steps import (AuthSteps,
                                     UsersSteps, VolumesSteps, SettingsSteps)

from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT, DASHBOARD_URL,
                     DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)
from .utils import create_demo_user, generate_ids


@pytest.fixture(params=('admin', 'demo'))
def any_user(request):
    if request.param == 'admin':
        os.environ['OS_LOGIN'] = ADMIN_NAME
        os.environ['OS_PASSWD'] = ADMIN_PASSWD
        os.environ['OS_PROJECT'] = ADMIN_PROJECT
    if request.param == 'demo':
        os.environ['OS_LOGIN'] = DEMO_NAME
        os.environ['OS_PASSWD'] = DEMO_PASSWD
        os.environ['OS_PROJECT'] = DEMO_PROJECT


@pytest.fixture
def admin_only():
    os.environ['OS_LOGIN'] = ADMIN_NAME
    os.environ['OS_PASSWD'] = ADMIN_PASSWD
    os.environ['OS_PROJECT'] = ADMIN_PROJECT


@pytest.yield_fixture(scope='session')
def horizon():
    app = Horizon(DASHBOARD_URL)
    create_demo_user(app)
    yield app
    app.quit()


@pytest.fixture
def auth_steps(horizon):
    return AuthSteps(horizon)


@pytest.yield_fixture
def login(auth_steps):
    auth_steps.login(os.environ['OS_LOGIN'], os.environ['OS_PASSWD'])
    auth_steps.switch_project(os.environ['OS_PROJECT'])
    yield
    auth_steps.logout()


@pytest.yield_fixture
def users_steps(auth_steps, horizon):
    auth_steps.login('admin', 'admin')
    yield UsersSteps(horizon)
    auth_steps.logout()


@pytest.yield_fixture
def volumes_steps(auth_steps, horizon):
    auth_steps.login('admin', 'admin')
    yield VolumesSteps(horizon)
    auth_steps.logout()


@pytest.yield_fixture
def settings_steps(auth_steps, horizon):
    auth_steps.login('admin', 'admin')
    yield SettingsSteps(horizon)
    auth_steps.logout()


@pytest.yield_fixture
def update_settings(settings_steps):
    current_settings = {}

    def _update_settings(lang=None, timezone=None, items_per_page=None,
                         instance_log_length=None):
        current_settings.update(settings_steps.current_settings)
        settings_steps.update_settings(lang, timezone, items_per_page,
                                       instance_log_length)

    yield _update_settings

    settings_steps.update_settings(**current_settings)


@pytest.yield_fixture
def create_volumes(volumes_steps):

    volumes = []

    def _create_volumes(names):
        for name in names:
            volumes_steps.create_volume(name)
            volumes.append(attrdict.AttrDict(name=name))

        return volumes

    yield volumes

    volumes_steps.delete_volumes(*[volume.name for volume in volumes])


@pytest.yield_fixture
def volume(volumes_steps):
    volume_name = generate_ids(prefix='volume').next()
    volumes_steps.create_volume(volume_name)
    volume = attrdict.AttrDict(name=volume_name)
    yield volume
    volumes_steps.delete_volume(volume.name)
