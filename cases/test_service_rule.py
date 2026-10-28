from selenium.webdriver.common.by import By
import time,pytest
from cfg import *
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def delAddedServiceModel(smpUI):
    print('** 删除添加的业务规则 setup **')

    yield

    print('** 删除添加的业务规则 teardown **')
    smpUI.del_first_item()

@pytest.fixture(scope='module')
def inServiceRuleManager(smpUI):
    print('** inServiceRuleManager setup **')
    smpUI.login('byhy', 'sdfsdf')
    smpUI.wd.get(SMP_URL_Service_Rule)

    yield

    print('** inServiceRuleManager **')


def test_SMP_Service_Rule_001(inServiceRuleManager,delAddedServiceModel,smpUI):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_service_rule(
        '规则1','预付费-下发业务量','50','100','度','1.5','电费'
    )

    dms = smpUI.get_first_page_service_rules()
    print("表格数据dms：", dms)
    assert dms == [[
        '规则1',
        '预付费-下发业务量',
        '最小消费50\n预估消费100\n费率\n单位：度 \n单价：1.5',
        '50'
    ]]











