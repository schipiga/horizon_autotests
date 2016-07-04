from pom import ui
from selenium.webdriver.common.by import By


class Form(ui.Form):

    submit_locator = By.CSS_SELECTOR, '*.btn.btn-primary'

    def submit(self):
        submit_button = self.webelement.find_element(*self.submit_locator)
        submit_button.click()
