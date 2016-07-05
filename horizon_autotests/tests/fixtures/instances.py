"""
Fixtures for instances.

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

from six import moves
from horizon_autotests.steps import InstancesSteps

from .utils import AttrDict, generate_ids

__all__ = [
    'create_instances',
    'instance',
    'instances_steps'
]


@pytest.yield_fixture
def create_instances(instances_steps):
    """Create instances."""
    instances = []

    def _create_instances(name, count=1):
        instances_steps.create_instance(name, count)
        if count == 1:
            instances.append(AttrDict(name=name))
        else:
            for i in moves.range(1, count + 1):
                instance_name = '{}-{}'.format(name, i)
                instances.append(AttrDict(name=instance_name))
        return instances

    yield _create_instances

    if instances:
        instances_steps.delete_instances(*[i.name for i in instances])


@pytest.fixture
def instances_steps(login, horizon):
    """Get instances steps."""
    return InstancesSteps(horizon)


@pytest.yield_fixture
def instance(instances_steps):
    """Create instance."""
    name = next(generate_ids('instance'))

    instances_steps.create_instance(name)
    instance = AttrDict(name=name)

    yield instance

    instances_steps.delete_instance(instance.name)
