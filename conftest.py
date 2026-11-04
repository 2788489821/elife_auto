import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

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