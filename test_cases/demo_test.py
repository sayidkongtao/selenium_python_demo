import pytest

import pytest


@pytest.fixture(scope='function', autouse=False)  # 作用域设置为class，自动运行
def before():
    print("->before")


class TestABC:

    def setup_class(self):
        self.a = 1
        print("->setup_class")

    def test_a(self, before):
        print("->test_a")
        print(self.a)
        assert 1

    def teardown(self):
        print("->teardown")

    def teardown_class(self):
        print("->teardown_class")


if __name__ == "__main__":
    pytest.main(["demo_test.py", "-s"])
