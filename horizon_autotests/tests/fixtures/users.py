"""
Fixtures for users.

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

from horizon_autotests.steps import UsersSteps

from .utils import AttrDict, generate_ids

__all__ = [
    'create_users',
    'user',
    'users_steps'
]


@pytest.fixture
def users_steps(login, horizon):
    """Get users steps."""
    return UsersSteps(horizon)


@pytest.yield_fixture
def create_users(users_steps):
    """Create users."""
    users = []

    def _create_users(names):
        for name in names:
            users_steps.create_user(name, name, 'admin')
            user = AttrDict(name=name, password=name)
            users.append(user)
        return users

    yield _create_users

    if users:
        users_steps.delete_users(*[user.name for user in users])


@pytest.fixture
def user(create_users):
    """Create user."""
    user_names = list(generate_ids('user'))
    return create_users(user_names)[0]
