from common.basetest import BaseTest
from pages.homepage import HomePage


class TestLogin(BaseTest):
    """登录测试"""

    def test_login(self):
        home_page = HomePage(self.driver, base_url=self.config["url"])
        home_page.go_home_page()
        home_page.login(self.config["username"], self.config["password"])


