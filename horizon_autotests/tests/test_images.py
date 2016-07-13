"""
Image tests.

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


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):
    """Tests for any user."""

    @pytest.mark.parametrize('images_count', [1, 2])
    def test_delete_images(self, images_count, create_images):
        """Verify that user can delete images as batch."""
        image_names = list(
            generate_ids('image', count=images_count, length=20))
        create_images(*image_names)

    def test_create_image_from_local_file(self):
        """Verify that user can create image from local file."""

    def test_view_image(self):
        """Verify that user can view image info."""

    def test_images_pagination(self):
        """Verify images pagination works right and back."""

    def test_update_image_metadata(self):
        """Verify that user can update image metadata."""

    def test_remove_protected_image(self):
        """Verify that user can't delete protected image."""

    def test_edit_image(self):
        """Verify that user ca edit image."""

    def test_create_volume_from_image(self):
        """Verify that user can create volume from image."""

    def test_edit_image_disk_and_ram_size(self):
        """Verify that image limits has influence to flavor choice."""


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):
    """Tests for admin only."""

    def test_public_image_visibility(self):
        """Verify that public image is visible for other users."""

    def test_launch_instance_from_image(self):
        """Verify that user can launch instance from image."""
