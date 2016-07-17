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
                                     UsersSteps)

from .config import (ADMIN_NAME,
                     ADMIN_PASSWD,
                     ADMIN_PROJECT,
                     DASHBOARD_URL,
                     DEMO_NAME,
                     DEMO_PASSWD,
                     DEMO_PROJECT)

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
        #_create_demo_user(app)
        yield app
        #_delete_demo_user(app)
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


def _create_demo_user(app):
    auth_steps = AuthSteps(app)
    auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
    auth_steps.switch_project(ADMIN_PROJECT)

    ProjectsSteps(app).create_project(DEMO_PROJECT)
    UsersSteps(app).create_user(DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

    auth_steps.logout()


def _delete_demo_user(app):
    auth_steps = AuthSteps(app)
    auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
    auth_steps.switch_project(ADMIN_PROJECT)

    UsersSteps(app).delete_user(DEMO_NAME)
    ProjectsSteps(app).delete_project(DEMO_PROJECT)

    auth_steps.logout()
