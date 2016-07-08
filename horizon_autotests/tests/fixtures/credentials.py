"""
Fixtures for credentials.

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

import os

import pytest

from .config import (ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT,
                     DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT)

__all__ = [
    'admin_only',
    'any_user',
    'demo_only'
]


@pytest.fixture(params=('admin', 'demo'))
def any_user(request):
    """Define user to log in account."""
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
    """Set admin credentials for test."""
    os.environ['OS_LOGIN'] = ADMIN_NAME
    os.environ['OS_PASSWD'] = ADMIN_PASSWD
    os.environ['OS_PROJECT'] = ADMIN_PROJECT


@pytest.fixture
def demo_only():
    """Set demo credentials for test."""
    os.environ['OS_LOGIN'] = DEMO_NAME
    os.environ['OS_PASSWD'] = DEMO_PASSWD
    os.environ['OS_PROJECT'] = DEMO_PROJECT
