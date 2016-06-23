import pytest


@pytest.mark.usefixtures('any_user')
class TestAnyUser(object):

    def test_floatingip_allocate(self, floatingip_steps):
        floatingip_steps.allocate_floatingip()

    def test_floatingip_associate(self, floatingip_steps):
        floatingip_steps.associate_floatingip()
