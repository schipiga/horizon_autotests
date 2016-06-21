import os

import pytest

from horizon_autotests.app import Horizon
from horizon_autotests.steps import AuthSteps, UsersSteps, VolumesSteps, SettingsSteps

DASHBOARD_URL = os.environ.get('DASHBOARD_URL')


@pytest.yield_fixture(scope='session')
def horizon():
    app = Horizon(DASHBOARD_URL)
    yield app
    app.quit()


@pytest.fixture
def auth_steps(horizon):
    return AuthSteps(horizon)


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
