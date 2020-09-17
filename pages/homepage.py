import allure
from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    """
    Home Page
    """

    # 请登录按钮
    login_btn = (By.CSS_SELECTOR, "#notlogindiv .notlogin a")

    @allure.step("进入到首页")
    def go_home_page(self):
        self.driver.get(self.base_url)

    @allure.step("从首页点登陆按钮，进入到登陆页面")
    def go_to_login_page(self):
        login_btn = self.wait_for_element_visible(self.login_btn)
        # 点击请登录按钮
        self.click(login_btn)


