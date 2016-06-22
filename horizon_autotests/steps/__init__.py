import os
import uuid

from six import moves

from .auth import AuthSteps
from .users import UsersSteps
from .volumes import VolumesSteps
from .settings import SettingsSteps


# TODO(svchipiga): maybe need to move it to another module.
def generate_ids(prefix=None, count=1):
    for _ in moves.range(count):
        uid = str(uuid.uuid4())
        if prefix:
            uid = '{}-{}'.format(prefix, uid)
        yield uid
