from .base import Block


class Form(Block):

    def submit(self):
        self.webelement.submit()
