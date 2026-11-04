import pytest
from pages.device_model_page import DeviceModelPage
from cfg import SMP_URL_Device_Model


@pytest.mark.parametrize('manager_page',
      [(DeviceModelPage, SMP_URL_Device_Model)], indirect=True)
def test_add_device_model_001(manager_page, clean_one_record):
    page = manager_page
    page.add_device_model('存储柜',
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小')

    dms = page.get_first_page_device_models()
    print("表格数据dms：", dms)
    target = ['存储柜',
              'elife-canbinlocker-g22-10-20-40',
              '南京e生活存储柜-10大20中40小']
    assert target in dms

@pytest.mark.parametrize('manager_page',
      [(DeviceModelPage, SMP_URL_Device_Model)], indirect=True)
def test_add_device_model_002(manager_page, clean_one_record):
    page = manager_page
    page.add_device_model('存储柜',
        '韩' * 100,
        '南京e生活存储柜-10大20中40小')

    dms = page.get_first_page_device_models()
    print("表格数据dms：", dms)
    target = ['存储柜',
        '韩' * 100,
        '南京e生活存储柜-10大20中40小']
    assert target in dms
