import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from cfg import *
from pages.device_model_page import DeviceModelPage
from pages.service_rule_page import ServiceRulePage

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)

    yield wd

    wd.quit()

@pytest.fixture()
def delAddedDeviceModel(driver):
    print('** 删除添加的设备型号 setup **')

    yield

    print('** 删除添加的设备型号 teardown **')

    page = DeviceModelPage(driver)
    page.del_first_item()
    page.close_add_form()

@pytest.fixture(scope='module')
def inDeviceModelManager(driver):
    print('** inDeviceModelManager setup **')
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    page.login('byhy', 'sdfsdf')
    page.wd.get(SMP_URL_Device_Model)

    yield

    print('** inDeviceModelManager **')

@pytest.fixture()
def delAddedServiceModel(driver):
    print('** 删除添加的业务规则 setup **')

    yield

    print('** 删除添加的业务规则 teardown **')

    page = ServiceRulePage(driver)
    page.del_first_item()
    page.close_add_form()

@pytest.fixture(scope='module')
def inServiceRuleManager(driver):
    print('** inServiceRuleManager setup **')
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    page.login('byhy', 'sdfsdf')
    page.wd.get(SMP_URL_Service_Rule)

    yield

    print('** inServiceRuleManager **')

@pytest.fixture
def clearAlert(driver):

    yield

    try:
        driver.switch_to.alert.accept()
    except Exception as e:
        print(e)