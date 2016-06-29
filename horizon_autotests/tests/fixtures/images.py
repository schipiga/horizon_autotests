import pytest

from horizon_autotests.steps import ImagesSteps

__all__ = [
    'images_steps'
]


@pytest.fixture
def images_steps(login, horizon):
    return ImagesSteps(horizon)
