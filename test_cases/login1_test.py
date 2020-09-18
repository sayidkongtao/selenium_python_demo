from common.basetest import BaseTest
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils.utils import Utils
import os
import allure


PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)


@allure.story('epic_1')
class TestLogin(BaseTest):
    """登录测试"""

    @allure.feature('feature_1:正常登陆测试')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("正常登陆测试")
    @allure.description("""
        step1:xxxxxx
        step2:xxxxxx
    """)
    def test_login(self, init):
        self.driver, self.config = init
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

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("登陆失败截图测试")
    @allure.description("""
        step1:xxxxxx
        step2:xxxxxx
    """)
    def test_login_failed(self, init):
        self.driver, self.config = init
        user = Utils.load_json_file(PATH(os.path.join(
            "..",
            "input_data",
            "user.json"
        )))
        home_page = HomePage(self.driver, base_url=self.config["url"])
        home_page.go_home_page()
        assert False
