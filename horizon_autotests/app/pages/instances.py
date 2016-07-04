from pom import ui
from selenium.webdriver.common.by import By

from horizon_autotests.app import ui as _ui

from .base import BasePage


@ui.register_ui(field_count=ui.TextField(By.NAME, 'count'),
                field_name=ui.TextField(By.NAME, 'name'))
class TabDetails(ui.Block):
    pass


class RadioVolumeCreate(ui.UI):

    @property
    def value(self):
        return self.webelement.find_element(
            By.XPATH, 'label[contains(@class, "active")]').text

    @value.setter
    def value(self, val):
        self.webelement.find_element(
            By.XPATH, 'label[text()="{}"]'.format(val)).click()


@ui.register_ui(
    button_add=ui.Button(By.CSS_SELECTOR, 'button.btn.btn-default'))
class RowAvailable(ui.Row):
    pass


class TableAvailableSources(ui.Table):
    columns = {'name': 2}
    Row = RowAvailable


@ui.register_ui(
    field_boot_source=ui.ComboBox(By.NAME, 'boot-source-type'),
    radio_volume_create=RadioVolumeCreate(
        By.XPATH,
        '//div[contains(@class, "btn-group") and label[@id="vol-create"]]'),
    table_available_sources=TableAvailableSources(
        By.CSS_SELECTOR, 'available table'))
class TabSource(ui.Block):
    pass


class TableAvailableFlavors(ui.Table):
    columns = {'name': 2}
    Row = RowAvailable


@ui.register_ui(
    table_available_flavors=TableAvailableFlavors(
        By.CSS_SELECTOR, 'available table'))
class TabFlavor(ui.Block):
    pass


class TableAvailableNetworks(ui.Table):
    columns = {'name': 2}
    Row = RowAvailable


@ui.register_ui(
    table_available_networks=TableAvailableNetworks(
        By.CSS_SELECTOR, 'available table'))
class TabNetwork(ui.Block):
    pass


@ui.register_ui(
    item_source=ui.UI(By.XPATH, '//li//span[text()="Source"]'),
    item_flavor=ui.UI(By.XPATH, '//li//span[text()="Flavor"]'),
    item_network=ui.UI(By.XPATH, '//li//span[text()="Networks"]'),
    tab_details=TabDetails(By.CSS_SELECTOR,
                           'ng-include[ng-form="launchInstanceDetailsForm"]'),
    tab_source=TabSource(By.CSS_SELECTOR,
                         'ng-include[ng-form="launchInstanceSourceForm"]'),
    tab_flavor=TabFlavor(By.CSS_SELECTOR,
                         'ng-include[ng-form="launchInstanceFlavorForm"]'),
    tab_network=TabNetwork(By.CSS_SELECTOR,
                           'ng-include[ng-form="launchInstanceNetworkForm"]'))
class FormLaunchInstance(_ui.Form):
    submit_locator = By.CSS_SELECTOR, 'button.btn.btn-primary.finish'


@ui.register_ui(
    lock_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_lock"]'),
    unlock_item=ui.UI(By.CSS_SELECTOR, '*[id*="action_unlock"]'))
class DropdownMenu(_ui.DropdownMenu):
    pass


@ui.register_ui(
    checkbox=_ui.CheckBox(By.CSS_SELECTOR, 'input[type="checkbox"]'),
    dropdown_actions=DropdownMenu())
class RowInstance(ui.Row):
    pass


class TableInstances(ui.Table):
    columns = {'name': 2, 'status': 7}
    Row = RowInstance


@ui.register_ui(
    button_delete_instances=ui.Button(By.ID, 'instances__action_delete'),
    button_launch_instance=ui.Button(By.ID, "instances__action_launch-ng"),
    form_launch_instance=FormLaunchInstance(
        By.CSS_SELECTOR,
        'wizard[ng-controller="LaunchInstanceWizardController"]'),
    table_instances=TableInstances(By.ID, 'instances'))
class InstancesPage(BasePage):
    url = "/project/instances/"
