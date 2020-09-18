from selenium import webdriver
from utils.utils import Utils
import os
import pytest

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)


class BaseTest(object):
    pass