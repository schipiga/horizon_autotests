import os

import pytest

from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                     DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

__all__ = [
    'admin_only',
    'any_user'
]


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
