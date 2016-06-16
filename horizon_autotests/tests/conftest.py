import os

import pytest

from horizon_autotests.app import Horizon
from horizon_autotests.steps import AuthSteps

DASHBOARD_URL = os.environ.get('DASHBOARD_URL')


@pytest.yield_fixture(scope='session')
def horizon():
    app = Horizon(DASHBOARD_URL)
    yield app
    app.quit()


@pytest.fixture
def auth_steps(horizon):
    return AuthSteps(horizon)
