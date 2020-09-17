from common.basetest import BaseTest
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils.utils import Utils
import os

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)


class TestLogin(BaseTest):
    """登录测试"""

    def test_login(self):
        user = Utils.load_json_file(PATH(os.path.join(
            "..",
            "input_data",
            "user.json"
        )))
        home_page = HomePage(self.driver, base_url=self.config["url"])
        home_page.go_home_page()
        home_page.go_to_login_page()

        login_page = LoginPage(self.driver)
        login_page.login(user["username"], user["password"])

    def test_login_failed(self):
        user = Utils.load_json_file(PATH(os.path.join(
            "..",
            "input_data",
            "user.json"
        )))
        home_page = HomePage(self.driver, base_url=self.config["url"])
        home_page.go_home_page()
        assert False
