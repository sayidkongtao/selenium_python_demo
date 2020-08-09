from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    """
    Home Page
    """

    # 请登录按钮
    login_btn = (By.CSS_SELECTOR, "#notlogindiv .notlogin a")

    # 用户名输入框
    user_name_input = (By.CSS_SELECTOR, ".account-login-main .login-name input")

    # 密码输入框
    password_input= (By.CSS_SELECTOR, ".account-login-main .login-password input")

    # 确认登录按钮
    confirm_login_btn = (By.CSS_SELECTOR, ".login-btn.active")

    # 下一次再说
    next_time_btn = (By.CSS_SELECTOR, ".next-time")

    def go_home_page(self):
        self.driver.get(self.base_url)

    def login(self, user_name, password):
        login_btn = self.wait_for_element_visible(self.login_btn)
        # 点击请登录按钮
        self.click(login_btn)
        # 输入用户名
        user_name_input = self.wait_for_element_visible(self.user_name_input)
        self.send_text(user_name_input, user_name)

        # 输入密码
        user_name_password_input = self.wait_for_element_visible(self.password_input)
        self.send_text(user_name_password_input, password)

        # 点击确认登录
        confirm_login_btn = self.wait_for_element_visible(self.confirm_login_btn)
        self.click(confirm_login_btn)

        try:
            next_time_btn = self.wait_for_element_visible(self.next_time_btn)
            if next_time_btn:
                self.click(next_time_btn)
        except Exception as e:
            pass


