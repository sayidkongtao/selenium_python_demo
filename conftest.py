import pytest
from selenium import webdriver
import os
import allure

from utils.utils import Utils

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)

driver = None
config = None


#初始化用例
@pytest.fixture(scope='session', autouse=False)
def init():
    print('init: ------------------')
    global driver
    global config
    if driver is None:
        config = Utils.load_config()
        driver = webdriver.Chrome(executable_path=PATH(os.path.join(
            "chrome_driver",
            "chromedriver.exe"
        )))
    yield driver, config
    print('结束用例')
    driver.close()
    driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    print('用例执行结果', outcome)

    # 从钩子方法的调用结果中获取测试报告
    report = outcome.get_result()

    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if report.when == "call" and report.failed:
        failed_path = PATH(
            os.path.join(
                "output",
                "failures"
            )
        )
        mode = "a" if os.path.exists(failed_path) else "w"

        with open(failed_path, mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(report.nodeid + extra + "\n")

        # 添加allure报告截图
        global driver
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
