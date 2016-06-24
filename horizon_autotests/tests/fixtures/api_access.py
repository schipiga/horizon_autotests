import pytest

from horizon_autotests.steps import ApiAccessSteps

__all__ = [
    'api_access_steps'
]


@pytest.fixture
def api_access_steps(login, horizon):
    return ApiAccessSteps(horizon)
