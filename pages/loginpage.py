from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class LoginPage(BasePage):
    """
    Login Page
    """

    # 用户名输入框
    user_name_input = (By.CSS_SELECTOR, ".account-login-main .login-name input")

    # 密码输入框
    password_input = (By.CSS_SELECTOR, ".account-login-main .login-password input")

    # 确认登录按钮
    confirm_login_btn = (By.CSS_SELECTOR, ".login-btn.active")

    # 下一次再说
    next_time_btn = (By.CSS_SELECTOR, ".next-time")

    @allure.step("登陆用户名：")
    def login(self, user_name, password):

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

        time.sleep(4)
