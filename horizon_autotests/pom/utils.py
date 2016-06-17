def register_ui(**ui):

    def wrapper(cls):
        cls.register_ui(**ui)
        return cls

    return wrapper


class Container(object):

    _registered_ui = None

    @classmethod
    def register_ui(cls, **ui):
        if not cls._registered_ui:
            cls._registered_ui = {}
        cls._registered_ui.update(ui)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def find_element(self, locator):
        return self.webelement.find_element(*locator)

    def find_elements(self, locator):
        return self.webelement.find_elements(*locator)

    def __getattr__(self, name):
        ui_obj = self._registered_ui.get(name)
        if not ui_obj:
            raise AttributeError("Attribute {!r} isn't defined".format(name))
        ui_obj.set_container(self)
        return ui_obj
