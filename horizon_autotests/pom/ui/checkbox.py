from .base import UI, immediately, wait_for_visibility


class CheckBox(UI):

    @property
    @immediately
    def is_selected(self):
        return self.webelement.is_selected()

    @wait_for_visibility
    def select(self):
        if not self.is_selected:
            self.webelement.click()

    @wait_for_visibility
    def unselect(self):
        if self.is_selected:
            self.webelement.click()
