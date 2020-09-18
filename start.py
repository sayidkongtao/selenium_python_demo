import pytest
import os

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)

if __name__ == '__main__':
    pytest.main(["--alluredir=./tmp/my_allure_results", "-s"])