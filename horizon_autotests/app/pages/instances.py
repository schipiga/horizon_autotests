from selenium.webdriver.common.by import By
from horizon_autotests import pom
from horizon_autotests.app import ui as _ui
from horizon_autotests.pom import ui

from .base import BasePage


@pom.register_ui(name_field=ui.TextField(By.NAME, 'name'),
                 count_field=ui.TextField(By.NAME, 'count'))
class DetailsTab(ui.Block):
    pass


class VolumeCreateRadio(ui.UI):

    @property
    def value(self):
        return self.webelement.find_element(
            By.XPATH, 'label[contains(@class, "active")]').text

    @value.setter
    def value(self, val):
        self.webelement.find_element(
            By.XPATH, 'label[text()="{}"]'.format(val)).click()


@pom.register_ui(
    add_button=ui.Button(By.CSS_SELECTOR, 'button.btn.btn-default'))
class AvailableRow(ui.Row):
    pass


class AvailableSourcesTable(ui.Table):
    columns = {'name': 2}
    Row = AvailableRow


@pom.register_ui(
    boot_source_field=ui.ComboBox(By.NAME, 'boot-source-type'),
    volume_create_radio=VolumeCreateRadio(
        By.XPATH,
        '//div[contains(@class, "btn-group") and label[@id="vol-create"]]'),
    available_sources_table=AvailableSourcesTable(
        By.CSS_SELECTOR, 'available table'))
class SourceTab(ui.Block):
    pass


class AvailableFlavorsTable(ui.Table):
    columns = {'name': 2}
    Row = AvailableRow


@pom.register_ui(
    available_flavors_table=AvailableFlavorsTable(
        By.CSS_SELECTOR, 'available table'))
class FlavorTab(ui.Block):
    pass


class AvailableNetworksTable(ui.Table):
    columns = {'name': 2}
    Row = AvailableRow


@pom.register_ui(
    available_networks_table=AvailableNetworksTable(
        By.CSS_SELECTOR, 'available table'))
class NetworkTab(ui.Block):
    pass


@pom.register_ui(
    source_item=ui.UI(By.XPATH, '//li//span[text()="Source"]'),
    flavor_item=ui.UI(By.XPATH, '//li//span[text()="Flavor"]'),
    network_item=ui.UI(By.XPATH, '//li//span[text()="Networks"]'),
    details_tab=DetailsTab(By.CSS_SELECTOR,
                           'ng-include[ng-form="launchInstanceDetailsForm"]'),
    source_tab=SourceTab(By.CSS_SELECTOR,
                         'ng-include[ng-form="launchInstanceSourceForm"]'),
    flavor_tab=FlavorTab(By.CSS_SELECTOR,
                         'ng-include[ng-form="launchInstanceFlavorForm"]'),
    network_tab=NetworkTab(By.CSS_SELECTOR,
                           'ng-include[ng-form="launchInstanceNetworkForm"]'))
class LaunchInstanceForm(_ui.Form):
    submit_locator = By.CSS_SELECTOR, 'button.btn.btn-primary.finish'


@pom.register_ui(
    toggle_button=ui.Button(By.CSS_SELECTOR, 'a.dropdown-toggle'),
    delete_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_delete"]'),
    lock_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_lock"]'),
    unlock_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_unlock"]'))
class DropdownActions(ui.Block):
    pass


@pom.register_ui(
    dropdown_actions=DropdownActions(By.CSS_SELECTOR, 'div.btn-group'),
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'))
class InstancesRow(ui.Row):
    pass


class InstancesTable(ui.Table):
    columns = {'name': 2, 'status': 7}
    Row = InstancesRow


@pom.register_ui(
    launch_instance_button=ui.Button(By.ID, "instances__action_launch-ng"),
    delete_instances_button=ui.Button(By.ID, 'instances__action_delete'),
    delete_instance_confirm_form=_ui.Form(By.CSS_SELECTOR,
                                          'div.modal-content'),
    launch_instance_form=LaunchInstanceForm(
        By.CSS_SELECTOR,
        'wizard[ng-controller="LaunchInstanceWizardController"]'),
    instances_table=InstancesTable(By.ID, 'instances'))
class InstancesPage(BasePage):
    url = "/project/instances/"
