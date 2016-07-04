from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui

from ..base import BasePage

from .tab_snapshots import TabSnapshots
from .tab_volumes import TabVolumes


@ui.register_ui(
    label_snapshots=ui.UI(By.CSS_SELECTOR, '[data-target$="snapshots_tab"]'),
    label_volumes=ui.UI(By.CSS_SELECTOR, '[data-target$="volumes_tab"]'),
    tab_snapshots=TabSnapshots(),
    tab_volumes=TabVolumes())
class VolumesPage(BasePage):
    url = "/project/volumes/"
    navigate_item = "Project", "Compute", "Volumes"
