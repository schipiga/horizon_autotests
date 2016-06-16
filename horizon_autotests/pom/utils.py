class Container(object):

    def find_element(self, locator):
        return self.web_element.find_element(*locator)

    def find_elements(self, locator):
        return self.web_element.find_elements(*locator)
