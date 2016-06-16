from horizon_autotests import pom


class Horizon(pom.App):

    def __init__(self, url, *args, **kwgs):
        super(Horizon, self).__init__(url, 'firefox', *args, **kwgs)
