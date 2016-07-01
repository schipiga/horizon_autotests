from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui


@ui.register_ui(
    next_link=ui.UI(By.CSS_SELECTOR, 'a[href^="?marker="]'),
    prev_link=ui.UI(By.CSS_SELECTOR, 'a[href^="?prev_marker="]'))
class Table(ui.Table):
    pass
