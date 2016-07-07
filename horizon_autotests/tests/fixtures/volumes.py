"""
Fixtures for volumes.

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

import pytest

from horizon_autotests.steps import VolumesSteps

from .utils import generate_ids, AttrDict

__all__ = [
    'create_snapshots',
    'create_volume',
    'create_volumes',
    'snapshot',
    'volume',
    'volumes_steps'
]


@pytest.fixture
def volumes_steps(login, horizon):
    """Get volumes steps."""
    return VolumesSteps(horizon)


@pytest.yield_fixture
def create_volumes(volumes_steps):
    """Create volumes."""
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
    """Create volume."""
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
    """Create volume."""
    volume_name = next(generate_ids('volume'))
    volumes_steps.create_volume(volume_name)
    volume = AttrDict(name=volume_name)
    yield volume
    volumes_steps.delete_volume(volume.name)


@pytest.yield_fixture
def snapshot(volume, volumes_steps):
    """Create snapshot."""
    snapshot_name = next(generate_ids('snapshot'))
    volumes_steps.create_snapshot(volume.name, snapshot_name)
    snapshot = AttrDict(name=snapshot_name)
    yield snapshot
    volumes_steps.delete_snapshot(snapshot.name)


@pytest.yield_fixture
def create_snapshots(volume, volumes_steps):
    """Create snapshots."""
    snapshots = []

    def _create_snapshots(snapshot_names):
        for snapshot_name in snapshot_names:
            volumes_steps.create_snapshot(volume.name, snapshot_name)
            snapshots.append(AttrDict(name=snapshot_name))

        return snapshots

    yield _create_snapshots

    if snapshots:
        volumes_steps.delete_snapshots(
            *[snapshot.name for snapshot in snapshots])


@pytest.yield_fixture
def create_snapshot(volume, volumes_steps):
    """Create snapshot."""
    snapshots = []

    def _create_volume(snapshot_name):
        volumes_steps.create_snapshot(volume.name, snapshot_name)
        snapshots.append(AttrDict(name=snapshot_name))
        return snapshots[-1]

    yield _create_volume

    for snapshot in snapshots:
        volumes_steps.delete_snapshot(snapshot.name)
