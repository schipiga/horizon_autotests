from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui

from .form import Form


@ui.register_ui(
    exit_item=ui.UI(By.CSS_SELECTOR, 'a[href*="/auth/logout/"]'))
class AccountDropdown(ui.Block):
    pass


class ProjectDropdown(ui.Block):

    def project_item(self, name):
        selector = ('//ul[contains(@class, "dropdown-menu")]/li//span[contains'
                    '(@class, "dropdown-title") and contains(., "{}")]'.format(
                        name))
        item = ui.UI(By.XPATH, selector)
        item.set_container(self)
        return item


class Spinner(ui.UI):

    def wait_for_absence(self, timeout=30):
        super(Spinner, self).wait_for_absence(timeout)


@ui.register_ui(
    account_dropdown=AccountDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav.navbar-right > li.dropdown'),
    project_dropdown=ProjectDropdown(
        By.CSS_SELECTOR, 'ul.navbar-nav > li.dropdown'),
    spinner=ui.UI(By.CSS_SELECTOR, 'div.modal-dialog'),
    form_confirm=Form(By.CSS_SELECTOR, 'div.modal-content'))
class InitiatedUI(ui.Container):
    pass
