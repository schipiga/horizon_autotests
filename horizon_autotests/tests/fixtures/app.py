"""
Fixtures to run horizon, login, create demo user, etc.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

from horizon_autotests.app import Horizon
from horizon_autotests.app.pages import PageLogin
from horizon_autotests.steps import (AuthSteps,
                                     ProjectsSteps,
                                     NetworksSteps,
                                     UsersSteps)

from ._config import (ADMIN_NAME,
                      ADMIN_PASSWD,
                      ADMIN_PROJECT,
                      DASHBOARD_URL,
                      DEFAULT_ADMIN_NAME,
                      DEFAULT_ADMIN_PASSWD,
                      DEFAULT_ADMIN_PROJECT,
                      SHARED_NETWORK_NAME,
                      USER_NAME,
                      USER_PASSWD,
                      USER_PROJECT)

__all__ = [
    'auth_steps',
    'horizon',
    'login'
]


@pytest.yield_fixture(scope='session')
def horizon():
    """Initial fixture.

    Starts browser and creates demo user before test.
    Deletes demo user and closes browser after test.
    """
    app = Horizon(DASHBOARD_URL)
    try:
        _create_test_env(app)
        yield app
        _delete_test_env(app)
    finally:
        app.quit()


@pytest.fixture
def auth_steps(horizon):
    """Get auth steps to login or logout in horizon."""
    return AuthSteps(horizon)


@pytest.yield_fixture
def login(auth_steps):
    """Login to horizon.

    Majority of tests requires user login. Logs out after test.
    """
    auth_steps.app.flush_session()  # delete cookies to force logout
    auth_steps.app.open(PageLogin)  # regenerate CSRF tokens

    auth_steps.login(os.environ['OS_LOGIN'], os.environ['OS_PASSWD'])
    auth_steps.switch_project(os.environ['OS_PROJECT'])

    yield

    auth_steps.logout()


def _create_test_env(app):
    auth_steps = AuthSteps(app)
    auth_steps.login(DEFAULT_ADMIN_NAME, DEFAULT_ADMIN_PASSWD)
    auth_steps.switch_project(DEFAULT_ADMIN_PROJECT)

    projects_steps = ProjectsSteps(app)
    projects_steps.create_project(ADMIN_PROJECT)
    projects_steps.create_project(USER_PROJECT)

    users_steps = UsersSteps(app)
    users_steps.create_user(ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                            role='admin')
    users_steps.create_user(USER_NAME, USER_PASSWD, USER_PROJECT)

    networks_steps = NetworksSteps(app)
    networks_steps.create_network(
        SHARED_NETWORK_NAME, shared=True, create_subnet=True)

    auth_steps.logout()


def _delete_test_env(app):
    auth_steps = AuthSteps(app)
    auth_steps.login(DEFAULT_ADMIN_NAME, DEFAULT_ADMIN_PASSWD)
    auth_steps.switch_project(DEFAULT_ADMIN_PROJECT)

    networks_steps = NetworksSteps(app)
    networks_steps.admin_delete_network(SHARED_NETWORK_NAME)

    users_steps = UsersSteps(app)
    users_steps.delete_user(USER_NAME)
    users_steps.delete_user(ADMIN_NAME)

    projects_steps = ProjectsSteps(app)
    projects_steps.delete_project(USER_PROJECT)
    projects_steps.delete_project(ADMIN_PROJECT)

    auth_steps.logout()
