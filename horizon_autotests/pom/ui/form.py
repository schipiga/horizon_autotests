from selenium.webdriver.common.by import By
from .base import Block


class Form(Block):

    def submit(self):
        self.webelement.submit()
