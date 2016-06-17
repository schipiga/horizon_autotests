from selenium.webdriver.common.by import By
from .base import Block


class Form(Block):

    def submit(self):
        submit_button = self.webelement.find_element(By.CSS_SELECTOR,
                                                     '*.btn.btn-primary')
        submit_button.click()
