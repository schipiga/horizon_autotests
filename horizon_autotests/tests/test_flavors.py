import pytest

from .utils import generate_ids


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    def test_flavor_update_metadata(self, flavor, flavors_steps):
            metadata = {
                generate_ids('metadata').next(): generate_ids("value").next()
                for i in range(2)}
            flavors_steps.update_flavor_metadata(flavor.name, metadata)

    def test_edit_flavor(self, flavor, flavors_steps):
        new_flavor_name = flavor.name + ' (updated)'
        with flavor.put(name=new_flavor_name):
            flavors_steps.update_flavor(name=flavor.name,
                                        new_name=new_flavor_name)

    def test_modify_flavor_access(self, flavor, flavors_steps):
        flavors_steps.modify_flavor_access(flavor.name)

    @pytest.mark.parametrize('flavors_count', [2, 1])
    def test_delete_flavors(self, flavors_count, create_flavors):
        flavor_names = list(generate_ids('flavor', count=flavors_count))
        create_flavors(flavor_names)
