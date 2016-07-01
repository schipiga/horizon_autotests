from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui

from .tab_admin_volumes import TabAdminVolumes
from .tab_volume_types import TabVolumeTypes

from ..base import BasePage


@ui.register_ui(
    label_admin_volumes=ui.UI(By.CSS_SELECTOR,
                              '[data-target$="volumes_tab"]'),
    label_volume_types=ui.UI(By.CSS_SELECTOR,
                             '[data-target$="volume_types_tab"]'),
    tab_admin_volumes=TabAdminVolumes(),
    tab_volume_types=TabVolumeTypes())
class AdminVolumesPage(BasePage):
    url = "/admin/volumes/"
