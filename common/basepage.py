from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver, base_url=""):
        self.driver = driver
        self.base_url = base_url

    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def send_text(element, value):
        element.send_keys(value)

    @staticmethod
    def get_text(element):
        return element.text

    @staticmethod
    def get_rect(element):
        return element.rect

    def tap(self, x, y):
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=int(x), y=int(y)).release().perform()

    def wait_for_element_visible(self, locator, time_out=30, poll_frequency=0.5, ignored_exceptions=None):
        driver_wait = WebDriverWait(self.driver, time_out, poll_frequency=poll_frequency,
                                    ignored_exceptions=ignored_exceptions)
        return driver_wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_presence(self, locator, time_out=30, poll_frequency=0.5, ignored_exceptions=None):
        driver_wait = WebDriverWait(self.driver, time_out, poll_frequency=poll_frequency,
                                    ignored_exceptions=ignored_exceptions)
        return driver_wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_invisible(self, locator, time_for_first_visible=5, time_out=30, poll_frequency=0.5,
                                   ignored_exceptions=None):
        driver_wait = WebDriverWait(self.driver, time_for_first_visible)
        try:
            driver_wait.until(EC.presence_of_element_located(locator))
        except:
            # ignore the error
            pass

        driver_wait = WebDriverWait(self.driver, time_out, poll_frequency=poll_frequency,
                                    ignored_exceptions=ignored_exceptions)
        driver_wait.until_not(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            return self.driver.find_element(locator[0], locator[1])
        except Exception as err:
            return False

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])