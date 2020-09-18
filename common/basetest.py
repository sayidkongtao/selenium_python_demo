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

    def setup_class(self):
        pass

    def teardown_class(self):
        pass
