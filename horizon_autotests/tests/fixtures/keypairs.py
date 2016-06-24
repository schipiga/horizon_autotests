import pytest

from horizon_autotests.steps import KeypairsSteps

from .utils import generate_ids, AttrDict

__all__ = [
    'import_keypair',
    'keypair',
    'keypairs_steps'
]


@pytest.fixture
def keypairs_steps(login, horizon):
    return KeypairsSteps(horizon)


@pytest.yield_fixture
def keypair(keypairs_steps):
    name = generate_ids('keypair').next()
    keypairs_steps.create_keypair(name)
    _keypair = AttrDict(name=name)

    yield _keypair

    keypairs_steps.delete_keypair(_keypair.name)


@pytest.yield_fixture
def import_keypair(keypairs_steps):
    keypairs = []

    def _import_keypair(public_key):
        name = generate_ids('keypair').next()
        keypairs_steps.import_keypair(name, public_key)
        keypair = AttrDict(name=name)
        keypairs.append(keypair)
        return keypair

    yield _import_keypair

    keypairs_steps.delete_keypairs(*[k.name for k in keypairs])
