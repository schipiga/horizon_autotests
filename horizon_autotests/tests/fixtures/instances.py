import attrdict
import pytest

from six import moves
from horizon_autotests.steps import InstancesSteps

from .utils import generate_ids

__all__ = [
    'create_instances',
    'instance',
    'instances_steps'
]


@pytest.yield_fixture
def create_instances(instances_steps):
    instances = []

    def _create_instances(name, count=1):
        instances_steps.create_instance(name, count)
        if count == 1:
            instances.append(attrdict.AttrDict(name=name))
        else:
            for i in moves.range(1, count + 1):
                instance_name = '{}-{}'.format(name, i)
                instances.append(attrdict.AttrDict(name=instance_name))
        return instances

    yield _create_instances

    if instances:
        instances_steps.delete_instances(*[i.name for i in instances])


@pytest.fixture
def instances_steps(login, horizon):
    return InstancesSteps(horizon)


@pytest.yield_fixture
def instance(instances_steps):
    name = generate_ids('instance').next()
    instances_steps.create_instance(name)
    instance = attrdict.AttrDict(name=name)
    yield instance
    instances_steps.delete_instance(instance.name)
