import pytest
from .fixtures.utils import generate_ids


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):

    @pytest.mark.parametrize('instances_count', [2, 1])
    def test_delete_instances(self, instances_count, create_instances):
        instance_name = generate_ids('instance').next()
        create_instances(instance_name, count=instances_count)

    def test_lock_instance(self, instance, instances_steps):
        instances_steps.lock_instance(instance.name)
        instances_steps.unlock_instance(instance.name)

# def test_view_instance(instance, instances_steps):
#     instances_steps.view_instance(instance.name)

    def test_instances_pagination(self, instances_steps, create_instances,
                                  update_settings):
        instance_name = generate_ids('instance').next()
        create_instances(instance_name, count=3)
        update_settings(items_per_page=1)


# def test_filter_instances(instances_steps, create_instances):
#     instance_name = generate_ids('instance').next()
#     instances = create_instances(instance_name, count=2)
#     instances_steps.filter_instances(query=instances[0].name)
