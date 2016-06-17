from selenium.webdriver.common.by import By

from horizon_autotests.pom import ui


class Form(ui.Form):

    def submit(self):
        submit_button = self.webelement.find_element(By.CSS_SELECTOR,
                                                     '*.btn.btn-primary')
        submit_button.click()
