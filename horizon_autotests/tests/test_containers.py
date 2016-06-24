import pytest
import requests

from .fixtures.utils import generate_ids, generate_files


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_create_public_container(self, create_container):
        container_name = generate_ids('container').next()
        create_container(container_name, public=True)

    def test_available_public_container_url(self, create_container,
                                            containers_steps):
        container_name = generate_ids('container').next()
        container = create_container(container_name, public=True)
        with containers_steps.container(container_name):
            folder_name = generate_ids('folder').next()
            containers_steps.create_folder(folder_name)
            assert folder_name in requests.get(container.link).text
            containers_steps.delete_folder(folder_name)

    def test_upload_file(self, container, containers_steps):
        with containers_steps.container(container.name):
            file_path = generate_files().next()
            file_name = containers_steps.upload_file(file_path)
            containers_steps.delete_file(file_name)

    def test_upload_file_to_folder(self, container, containers_steps):
        with containers_steps.container(container.name):
            folder_name = generate_ids('folder').next()
            containers_steps.create_folder(folder_name)
            with containers_steps.folder(folder_name):
                file_path = generate_files().next()
                file_name = containers_steps.upload_file(file_path)
                containers_steps.delete_file(file_name)
            containers_steps.delete_folder(folder_name)
