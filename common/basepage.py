from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver, base_url=""):
        self.driver = driver
        self.base_url = base_url
        self.time_out = 30
        self.webdriver_wait = WebDriverWait(self.driver, self.time_out)

    def click(self, element):
        element.click()

    def send_text(self, element, value):
        element.send_keys(value)

    def get_text(self, element):
        return element.text

    def wait_for_element_visible(self, locator):
        return self.webdriver_wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_presence(self, locator):
        return self.webdriver_wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            return self.driver.find_element(locator[0], locator[1])
        except Exception as err:
            return False

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])


