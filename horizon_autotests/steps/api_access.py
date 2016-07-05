from horizon_autotests.app.pages import PageAccess

from .base import BaseSteps


class ApiAccessSteps(BaseSteps):

    def api_access_page(self):
        access_page = self._open(PageAccess)
        access_page.api_access_tab.click()
        return access_page

    def download_v2_file(self):
        page = self.api_access_page()
        page.download_v2_file_button.click()

        # assert 'OS_USERNAME' in v2_content
        # assert 'OS_TENANT_NAME' in v2_content
        # assert 'OS_TENANT_ID' in v2_content

    def download_v3_file(self):
        page = self.api_access_page()
        page.download_v3_file_button.click()

        # assert 'OS_USERNAME' in v3_content
        # assert 'OS_TENANT_NAME' in v3_content
        # assert 'OS_TENANT_ID' in v3_content

    def view_credentials(self):
        page = self.api_access_page()
        page.view_credentials_button.click()
