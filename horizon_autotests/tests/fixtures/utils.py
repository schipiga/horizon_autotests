import uuid

import attrdict
from six import moves

from horizon_autotests.steps import AuthSteps, ProjectsSteps, UsersSteps


def generate_ids(prefix=None, count=1, length=None):
    for _ in moves.range(count):
        uid = str(uuid.uuid4())
        if prefix:
            uid = '{}-{}'.format(prefix, uid)
        if length:
            uid = uid[0:length]
        yield uid


def generate_files():
    pass


def slugify(string):
    return ''.join(s if s.isalnum() else '_' for s in string).strip('_')


def create_demo_user(app):
    from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                         DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

    auth_steps = AuthSteps(app)
    auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
    auth_steps.switch_project(ADMIN_PROJECT)

    projects_steps = ProjectsSteps(app)
    projects_steps.create_project(DEMO_PROJECT)

    users_steps = UsersSteps(app)
    users_steps.create_user(DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

    auth_steps.logout()


def delete_demo_user(app):
    from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                         DEMO_NAME, DEMO_PROJECT)

    auth_steps = AuthSteps(app)
    auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
    auth_steps.switch_project(ADMIN_PROJECT)

    users_steps = UsersSteps(app)
    users_steps.delete_user(DEMO_NAME)

    projects_steps = ProjectsSteps(app)
    projects_steps.delete_project(DEMO_PROJECT)

    auth_steps.logout()


class AttrDict(attrdict.AttrDict):

    _updated_fields = {}

    def __init__(self, *args, **kwgs):
        super(AttrDict, self).__init__(*args, **kwgs)

    def put(self, **kwgs):
        self._updated_fields[id(self)] = kwgs
        return self

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        updated_fields = self._updated_fields.pop(id(self))
        self.update(updated_fields)
