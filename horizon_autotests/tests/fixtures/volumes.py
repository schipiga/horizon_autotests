import pytest

from horizon_autotests.steps import VolumesSteps

from .utils import generate_ids, AttrDict

__all__ = [
    'create_volume',
    'create_volumes',
    'snapshot',
    'volume',
    'volumes_steps'
]


@pytest.fixture
def volumes_steps(login, horizon):
    return VolumesSteps(horizon)


@pytest.yield_fixture
def create_volumes(volumes_steps):
    volumes = []

    def _create_volumes(names):
        for name in names:
            volumes_steps.create_volume(name)
            volumes.append(AttrDict(name=name))

        return volumes

    yield _create_volumes

    if volumes:
        volumes_steps.delete_volumes(*[volume.name for volume in volumes])


@pytest.yield_fixture
def create_volume(volumes_steps):
    volumes = []

    def _create_volume(name, volume_type):
        volumes_steps.create_volume(name, volume_type=volume_type)
        volumes.append(AttrDict(name=name))
        return volumes[-1]

    yield _create_volume

    for volume in volumes:
        volumes_steps.delete_volume(volume.name)


@pytest.yield_fixture
def volume(volumes_steps):
    volume_name = generate_ids(prefix='volume').next()
    volumes_steps.create_volume(volume_name)
    volume = AttrDict(name=volume_name)
    yield volume
    volumes_steps.delete_volume(volume.name)


@pytest.yield_fixture
def snapshot(volume, volumes_steps):
    snapshot_name = generate_ids('snapshot').next()
    volumes_steps.create_snapshot(volume.name, snapshot_name)
    snapshot = AttrDict(name=snapshot_name)
    yield snapshot
    volumes_steps.delete_snapshot(snapshot.name)
