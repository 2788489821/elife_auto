from selenium.webdriver.common.by import By
import time,pytest
from cfg import *
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def delAddedDeviceModel(smpUI):
    print('** 删除添加的设备型号 setup **')
    yield

    print('** 删除添加的设备型号 teardown **')
    smpUI.del_first_item()

@pytest.fixture(scope='module')
def inDeviceModelManager(smpUI):
    print('** inDeviceModelManager setup **')
    smpUI.login('byhy', 'sdfsdf')
    smpUI.wd.get(SMP_URL_Device_Model)

    yield

    print('** inDeviceModelManager **')


def test_SMP_Device_model_001(inDeviceModelManager,delAddedDeviceModel,smpUI):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model(
        '存储柜',
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小'
    )

    dms = smpUI.get_first_page_device_models()
    print("表格数据dms：", dms)
    assert dms == [[
        '存储柜',
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小'
    ]]

def test_SMP_Device_model_002(inDeviceModelManager,delAddedDeviceModel,smpUI):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model(
        '存储柜',
        '韩'*100,
        '南京e生活存储柜-10大20中40小'
    )

    dms = smpUI.get_first_page_device_models()
    print("表格数据dms：", dms)
    assert dms == [[
        '存储柜',
        '韩'*100,
        '南京e生活存储柜-10大20中40小'
    ]]











