import time


class Waiter(object):

    def __init__(self, polling=0.05):
        self._polling = polling

    def exe(self, timeout, func, *args, **kwgs):
        if not timeout:
            return func(*args, **kwgs) or False
        limit = int(time.time()) + timeout
        while int(time.time()) <= limit:
            result = func(*args, **kwgs)
            if result:
                return result
            time.sleep(self._polling)
        return False
