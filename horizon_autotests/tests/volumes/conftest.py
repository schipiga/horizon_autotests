import attrdict
import pytest
from horizon_autotests.steps import generate_ids


@pytest.yield_fixture
def volume(volumes_steps):
    volume_name = generate_ids(prefix='volume').next()
    volumes_steps.create_volume(volume_name)
    volume = attrdict.AttrDict(name=volume_name)
    yield volume
    volumes_steps.delete_volume(volume.name)
