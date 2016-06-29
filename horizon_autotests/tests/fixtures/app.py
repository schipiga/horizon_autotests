import os

import pytest

from horizon_autotests.app import Horizon
from horizon_autotests.steps import AuthSteps

from .config import DASHBOARD_URL
from .utils import create_demo_user, delete_demo_user

__all__ = [
    'auth_steps',
    'horizon',
    'login'
]


@pytest.yield_fixture(scope='session')
def horizon():
    app = Horizon(DASHBOARD_URL)
    #create_demo_user(app)
    yield app
    #delete_demo_user(app)
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
