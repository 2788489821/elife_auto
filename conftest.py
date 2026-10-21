import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.webUI_smp import SMP_UI

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    yield wd

    wd.quit()

@pytest.fixture(scope="module")
def smpUI(driver):
    page = SMP_UI(driver)
    yield page
