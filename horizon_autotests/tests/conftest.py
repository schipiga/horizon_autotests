import logging
import os

import attrdict
import pytest
import xvfbwrapper

from six import moves
from horizon_autotests.app import Horizon
from horizon_autotests.steps import (AuthSteps,
                                     UsersSteps,
                                     VolumesSteps,
                                     InstancesSteps,
                                     SettingsSteps,
                                     VolumeTypesSteps)
from horizon_autotests.third_party import VideoRecorder

from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT, DASHBOARD_URL,
                     DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT, VIRTUAL_DISPLAY)
from .utils import create_demo_user, generate_ids

LOGGER = logging.getLogger(__name__)


@pytest.fixture(params=('admin', 'demo'))
def any_user(request):
    if request.param == 'admin':
        os.environ['OS_LOGIN'] = ADMIN_NAME
        os.environ['OS_PASSWD'] = ADMIN_PASSWD
        os.environ['OS_PROJECT'] = ADMIN_PROJECT
    if request.param == 'demo':
        os.environ['OS_LOGIN'] = DEMO_NAME
        os.environ['OS_PASSWD'] = DEMO_PASSWD
        os.environ['OS_PROJECT'] = DEMO_PROJECT


@pytest.fixture
def admin_only():
    os.environ['OS_LOGIN'] = ADMIN_NAME
    os.environ['OS_PASSWD'] = ADMIN_PASSWD
    os.environ['OS_PROJECT'] = ADMIN_PROJECT


@pytest.fixture(scope="session")
def virtual_display(request):
    if not VIRTUAL_DISPLAY:
        return

    _virtual_display = xvfbwrapper.Xvfb(width=1920, height=1080)
    # workaround for memory leak in Xvfb taken from:
    # http://blog.jeffterrace.com/2012/07/xvfb-memory-leak-workaround.html
    # and disables X access control
    args = ["-noreset", "-ac"]

    if hasattr(_virtual_display, 'extra_xvfb_args'):
        _virtual_display.extra_xvfb_args.extend(args)  # xvfbwrapper>=0.2.8
    else:
        _virtual_display.xvfb_cmd.extend(args)

    _virtual_display.start()

    def fin():
        LOGGER.info('Stop xvfb')
        _virtual_display.stop()

    request.addfinalizer(fin)


@pytest.yield_fixture(scope='session')
def video_capture(virtual_display):
    recorder = VideoRecorder()
    recorder.start()

    yield recorder

    LOGGER.info("Stop video recording")
    recorder.stop()


@pytest.yield_fixture(scope='session')
def horizon(video_capture):
    app = Horizon(DASHBOARD_URL)
    # create_demo_user(app)
    yield app
    app.quit()


@pytest.fixture
def auth_steps(horizon):
    return AuthSteps(horizon)


@pytest.yield_fixture
def login(auth_steps):
    auth_steps.login(os.environ['OS_LOGIN'], os.environ['OS_PASSWD'])
    auth_steps.switch_project(os.environ['OS_PROJECT'])
    yield
    auth_steps.logout()


@pytest.fixture
def users_steps(login, horizon):
    return UsersSteps(horizon)


@pytest.fixture
def volumes_steps(login, horizon):
    return VolumesSteps(horizon)


@pytest.fixture
def settings_steps(login, horizon):
    return SettingsSteps(horizon)


@pytest.yield_fixture
def update_settings(settings_steps):
    current_settings = {}

    def _update_settings(lang=None, timezone=None, items_per_page=None,
                         instance_log_length=None):
        current_settings.update(settings_steps.current_settings)
        settings_steps.update_settings(lang, timezone, items_per_page,
                                       instance_log_length)

    yield _update_settings

    settings_steps.update_settings(**current_settings)


@pytest.yield_fixture
def create_volumes(volumes_steps):
    volumes = []

    def _create_volumes(names):
        for name in names:
            volumes_steps.create_volume(name)
            volumes.append(attrdict.AttrDict(name=name))

        return volumes

    yield _create_volumes

    if volumes:
        volumes_steps.delete_volumes(*[volume.name for volume in volumes])


@pytest.yield_fixture
def volume(volumes_steps):
    volume_name = generate_ids(prefix='volume').next()
    volumes_steps.create_volume(volume_name)
    volume = attrdict.AttrDict(name=volume_name)
    yield volume
    volumes_steps.delete_volume(volume.name)


@pytest.yield_fixture
def create_users(users_steps):
    users = []

    def _create_users(names):
        for name in names:
            users_steps.create_user(name, name, 'admin')
            users.append(attrdict.AttrDict(name=name, password=name))
        return users

    yield _create_users

    if users:
        users_steps.delete_users(*[user.name for user in users])


@pytest.fixture
def user(create_users):
    user_names = list(generate_ids('user'))
    return create_users(user_names)[0]


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
