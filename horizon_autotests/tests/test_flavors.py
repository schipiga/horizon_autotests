"""
Flavor tests.

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

from .fixtures.utils import generate_ids


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):
    """Tests for admin only."""

    def test_flavor_update_metadata(self, flavor, flavors_steps):
        """Verify that admin can update flavor metadata."""
        metadata = {
            next(generate_ids('metadata')): next(generate_ids("value"))
            for i in range(2)}
        flavors_steps.update_flavor_metadata(flavor.name, metadata)

    def test_update_flavor(self, flavor, flavors_steps):
        """Verify that admin cat update flavor."""
        new_flavor_name = flavor.name + ' (updated)'
        with flavor.put(name=new_flavor_name):
            flavors_steps.update_flavor(name=flavor.name,
                                        new_name=new_flavor_name)

    def test_modify_flavor_access(self, flavor, flavors_steps):
        """Verify that admin can modify flavor access."""
        flavors_steps.modify_flavor_access(flavor.name)

    @pytest.mark.parametrize('flavors_count', [2, 1])
    def test_delete_flavors(self, flavors_count, create_flavors):
        """Verify that admin can delete flavors as batch."""
        flavor_names = list(generate_ids('flavor', count=flavors_count))
        create_flavors(flavor_names)
