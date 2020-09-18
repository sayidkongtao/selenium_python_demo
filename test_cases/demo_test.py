from common.basetest import BaseTest
from conftest import setup_module, setup_session


class TestDemo(BaseTest):

    def test_1(self, setup_session, setup_module):
        print("test1--------------")
        print("a: " + self.a)