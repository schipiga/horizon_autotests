from .base import UI


class TextField(UI):

    @property
    def value(self):
        return self.webelement.text

    @value.setter
    def value(self, text):
        self.webelement.clear()
        self.webelement.send_keys(text)
