from common.basetest import BaseTest
from conftest import setup_module, setup_session


class TestDemo(BaseTest):

    def test_2(self, setup_session, setup_module):
        print("test2--------------")
        print("a: " + self.a)

    def test_3(self, setup_session, setup_module):
        print("test3--------------")
        print("a: " + self.a)
