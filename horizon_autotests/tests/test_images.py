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

from .fixtures.utils import generate_ids, generate_files


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):
    """Tests for any user."""

    @pytest.mark.parametrize('images_count', [1, 2])
    def test_delete_images(self, images_count, create_images):
        """Verify that user can delete images as batch."""
        image_names = list(
            generate_ids('image', count=images_count, length=20))
        create_images(*image_names)

    def test_create_image_from_local_file(self, create_image):
        """Verify that user can create image from local file."""
        image_name = next(generate_ids('image', length=20))
        image_file = next(generate_files(postfix='.qcow2'))
        create_image(image_name, image_file)

    def test_view_image(self):
        """Verify that user can view image info."""

    def test_images_pagination(self, images_steps, create_images,
                               update_settings):
        """Verify images pagination works right and back."""
        image_names = sorted(list(generate_ids('image', count=2, length=20)))
        create_images(*image_names)
        update_settings(items_per_page=1)

        page_images = images_steps.page_images()

        page_images.table_images.row(name=image_names[0]).wait_for_presence()
        assert page_images.table_images.link_next.is_present
        assert not page_images.table_images.link_prev.is_present

        page_images.table_images.link_next.click()

        page_images.table_images.row(name=image_names[1]).wait_for_presence()
        assert page_images.table_images.link_next.is_present
        assert page_images.table_images.link_prev.is_present

        page_images.table_images.link_next.click()

        page_images.table_images.row(name='TestVM').wait_for_presence()
        assert not page_images.table_images.link_next.is_present
        assert page_images.table_images.link_prev.is_present

        page_images.table_images.link_prev.click()

        page_images.table_images.row(name=image_names[1]).wait_for_presence()
        assert page_images.table_images.link_next.is_present
        assert page_images.table_images.link_prev.is_present

        page_images.table_images.link_prev.click()

        page_images.table_images.row(name=image_names[0]).wait_for_presence()
        assert page_images.table_images.link_next.is_present
        assert not page_images.table_images.link_prev.is_present

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
