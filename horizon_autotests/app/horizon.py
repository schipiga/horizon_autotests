"""
Horizon application implementation.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pom

from .pages import PageBase, pages


class Horizon(pom.App):
    """Application to launch horizon in browser."""

    def __init__(self, url, *args, **kwgs):
        """Constructor."""
        super(Horizon, self).__init__(url, 'firefox', *args, **kwgs)
        self.webdriver.maximize_window()
        self.webdriver.set_window_size(1920, 1080)
        self.webdriver.implicitly_wait(5)
        self.webdriver.set_page_load_timeout(30)

    def open(self, page):
        """Open page or url.

        Arguments:
            - page: page class or url string.
        """
        if isinstance(page, str):
            url = page
        else:
            url = page.url
        super(Horizon, self).open(url)

    @property
    def current_page(self):
        """Current page dynamic definition."""
        current_url = self.webdriver.current_url
        for page in pages:
            url = self.app_url + page.url

            if current_url.startswith(url):
                url_end = current_url.split(url)[-1]

                if not (url_end and url_end[0].isalnum()):
                    return page(self)
        return PageBase(self)

    def flush_session(self):
        """Delete all cookies.

        It forces flushes user session by cookies deleting.
        """
        self.webdriver.delete_all_cookies()
