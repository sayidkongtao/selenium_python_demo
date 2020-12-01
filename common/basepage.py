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
            self.webdriver_wait.until_not(EC.presence_of_element_located(locator))
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

    def swipe_up(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.swipe(x1, y1, x2, y1, t)

    def swipe(self, x1, y1, x2, y2, t):
        self.driver.swipe(x1, y1, x2, y2, t)
