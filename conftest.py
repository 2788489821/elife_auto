# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import os
import time
from pathlib import Path  # 新增导入Path

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)

    yield wd

    wd.quit()


@pytest.fixture(scope="module")
def manager_page(driver, request):
    page_cls, url = request.param
    LoginPage(driver).login('byhy', 'sdfsdf')
    driver.get(url)

    yield page_cls(driver)
    # page = page_cls
    # 这里可以放整个用例文件执行完之后的后续收尾操作,现在的需求的后续操作都是每个用例结束后都要做的操作，所以这里先不写。


@pytest.fixture
def clearAlert(driver):
    yield
    try:
        driver.switch_to.alert.accept()
    except Exception as e:
        print(e)


@pytest.fixture()
def clean_one_record(manager_page):
    yield
    manager_page.del_first_item()


@pytest.fixture()
def close_add_form(manager_page):
    yield
    try:
        manager_page.close_add_form()
    except Exception:
        pass


# 失败自动截图钩子
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 用例执行阶段失败则截图
    if report.when == 'call' and report.failed:
        # 拿driver
        driver = item.funcargs.get('driver', None)
        if driver is None:
            print('当前用例没有driver，无法截图')
            return

        # 截图存放位置，未识别到文件夹则自动创建，且基于当前文件位置使用绝对路径
        screenshot_dir = Path(__file__).parent / "screenshots"
        if not screenshot_dir.exists():
            screenshot_dir.mkdir(parents=True, exist_ok=True)

        # %f 微秒，避免同一秒覆盖
        case_name = item.name
        timestamp = time.strftime("%Y%m%d_%H%M%S_%f")
        file_name = f'{case_name}_{timestamp}.png'
        save_path = screenshot_dir / file_name

        # 保存截图
        try:
            driver.save_screenshot(str(save_path))
            print(f'【失败截图已保存】{save_path}')
        except Exception as e:
            print(f'【截图失败：】{e}')
