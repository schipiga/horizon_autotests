from pom import ui
from selenium.webdriver.common.by import By


@ui.register_ui(
    link_next=ui.UI(By.CSS_SELECTOR, 'a[href^="?marker="]'),
    link_prev=ui.UI(By.CSS_SELECTOR, 'a[href^="?prev_marker="]'))
class Table(ui.Table):
    pass
