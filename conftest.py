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

    page = page_cls(driver)
    page.del_first_item()
    # page.close_add_form()

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

# @pytest.fixture()
# def close_add_form(manager_page):
#     yield
#     try:
#         manager_page.close_add_form()
#     except Exception:
#         pass
