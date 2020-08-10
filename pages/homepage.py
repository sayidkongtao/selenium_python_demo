from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    """
    Home Page
    """

    # 请登录按钮
    login_btn = (By.CSS_SELECTOR, "#notlogindiv .notlogin a")

    def go_home_page(self):
        self.driver.get(self.base_url)

    def go_to_login_page(self):
        login_btn = self.wait_for_element_visible(self.login_btn)
        # 点击请登录按钮
        self.click(login_btn)


