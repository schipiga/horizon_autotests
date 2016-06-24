import pytest

from horizon_autotests.steps import SettingsSteps

__all__ = [
    'settings_steps',
    'update_settings'
]


@pytest.fixture
def settings_steps(login, horizon):
    return SettingsSteps(horizon)


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
