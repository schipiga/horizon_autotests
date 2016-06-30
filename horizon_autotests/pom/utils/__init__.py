from .waiter import Waiter  # noqa


def cache(func):
    attrname = '_cached_' + func.__name__

    def wrapper(self, *args, **kwgs):
        result = getattr(self, attrname, None)
        if not result:
            result = func(self, *args, **kwgs)
            setattr(self, attrname, result)
        return result

    return wrapper
