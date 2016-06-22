import uuid

from six import moves

from horizon_autotests.steps import AuthSteps, ProjectsSteps, UsersSteps


def generate_ids(prefix=None, count=1):
    for _ in moves.range(count):
        uid = str(uuid.uuid4())
        if prefix:
            uid = '{}-{}'.format(prefix, uid)
        yield uid


def create_demo_user(app):
    from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                         DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

    auth_steps = AuthSteps(app)
    auth_steps.login(ADMIN_NAME, ADMIN_PASSWD)
    auth_steps.switch_project(ADMIN_PROJECT)

    projects_steps = ProjectsSteps(app)
    if projects_steps.projects_page \
            .projects_table.row(name=DEMO_PROJECT).is_present:
        projects_steps.delete_project(DEMO_PROJECT)
    projects_steps.create_project(DEMO_PROJECT)

    users_steps = UsersSteps(app)
    if users_steps.users_page.users_table.row(name=DEMO_NAME).is_present:
        users_steps.delete_user(DEMO_NAME)
    users_steps.create_user(DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

    auth_steps.logout()
