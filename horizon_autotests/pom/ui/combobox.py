from selenium.webdriver.support.ui import Select

from .base import UI


class ComboBox(UI):

    @property
    def webelement(self):
        return Select(super(ComboBox, self).webelement)

    @property
    def value(self):
        return self.webelement.first_selected_option.text

    @value.setter
    def value(self, value):
        self.webelement.select_by_visible_text(value)

    @property
    def values(self):
        return [o.text for o in self.webelement.options]
