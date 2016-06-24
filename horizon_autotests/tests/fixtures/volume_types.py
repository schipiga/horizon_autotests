import attrdict
import pytest

from horizon_autotests.steps import VolumeTypesSteps

from .utils import generate_ids

__all__ = [
    'qos_spec',
    'volume_type',
    'volume_types_steps'
]


@pytest.fixture
def volume_types_steps(login, horizon):
    return VolumeTypesSteps(horizon)


@pytest.yield_fixture
def volume_type(volume_types_steps):
    name = generate_ids('volume-type').next()
    volume_types_steps.create_volume_type(name)
    _volume_type = attrdict.AttrDict(name=name)
    yield _volume_type
    volume_types_steps.delete_volume_type(_volume_type.name)


@pytest.yield_fixture
def qos_spec(volume_types_steps):
    name = generate_ids('qos-spec').next()
    volume_types_steps.create_qos_spec(name)
    _qos_spec = attrdict.AttrDict(name=name)
    yield _qos_spec
    volume_types_steps.delete_qos_spec(_qos_spec.name)
