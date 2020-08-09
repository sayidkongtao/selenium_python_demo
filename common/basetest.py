from selenium import webdriver
from utils.utils import Utils
import os

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)

class BaseTest(object):

    def setup(self):
        self.config = Utils.load_config()
        self.driver = webdriver.Chrome(executable_path=PATH(os.path.join(
            "..",
            "chrome_driver",
            "chromedriver"
        )))

    def teardown(self):
        self.driver.close()
