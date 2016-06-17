from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui


class CheckBox(ui.CheckBox):

    @property
    def label(self):
        web_id = self.webelement.get_attribute('id')
        label_locator = By.CSS_SELECTOR, 'label[for="{}"]'.format(web_id)
        return self.container.find_element(label_locator)

    @property
    @ui.immediately
    def is_selected(self):
        return self.webelement.is_selected()

    def select(self):
        if not self.is_selected:
            self.label.click()

    def unselect(self):
        if self.is_selected:
            self.label.click()
