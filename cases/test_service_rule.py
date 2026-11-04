import pytest
from pages.service_rule_page import ServiceRulePage
from cfg import SMP_URL_Service_Rule

@pytest.mark.parametrize('manager_page',
      [(ServiceRulePage, SMP_URL_Service_Rule)], indirect=True)
def test_SMP_Service_Rule_001(manager_page, clean_one_record, close_add_form):
    page = manager_page
    page.add_service_rule(
        '规则1','预付费-下发业务量','50','100','度','1.5','电费'
    )

    dms = page.get_first_page_service_rules()
    print("表格数据dms：", dms)
    target = [
        '规则1',
        '预付费-下发业务量',
        '最小消费50\n预估消费100\n费率\n单位：度 \n单价：1.5',
        '50'
    ]
    assert target in dms


@pytest.mark.parametrize('manager_page',
      [(ServiceRulePage, SMP_URL_Service_Rule)], indirect=True)
def test_SMP_Service_Rule_002(manager_page, clean_one_record, close_add_form):
    page = manager_page
    page.add_service_rule(
        '规则2','预付费-下发费用','200','3000','','','重量',''
    )

    dms = page.get_first_page_service_rules()
    print("表格数据dms：", dms)
    target = [
        '规则2',
        '预付费-下发费用',
        '最小消费200\n预估消费3000',
        '200'
    ]
    assert target in dms

@pytest.mark.parametrize('manager_page',
      [(ServiceRulePage, SMP_URL_Service_Rule)], indirect=True)
def test_SMP_Service_Rule_003(manager_page, clean_one_record, close_add_form):
    page = manager_page
    page.add_service_rule(
        '规则3','后付费-上报业务量','','','','','重量',[('00001','kg','77.45')]
    )

    dms = page.get_first_page_service_rules()
    print("表格数据dms：", dms)
    target = [
        '规则3',
        '后付费-上报业务量',
        '费率\n业务码：00001\n单位：kg \n单价：77.45',
        '重量'
    ]
    assert target in dms

@pytest.mark.parametrize('manager_page',
      [(ServiceRulePage, SMP_URL_Service_Rule)], indirect=True)
def test_SMP_Service_Rule_004(manager_page, clean_one_record, close_add_form):
    page = manager_page
    page.add_service_rule(
        '规则4','后付费-上报业务量','','','','','重量',[('00001','kg','77.45'),('00003','kg','799'),('00094','t','5000123456')]
    )

    dms = page.get_first_page_service_rules()
    print("表格数据dms：", dms)
    target = [
        '规则4',
        '后付费-上报业务量',
        '费率\n'
        '业务码：00001\n'
        '单位：kg \n'
        '单价：77.45\n'
        '业务码：00003\n'
        '单位：kg \n'
        '单价：799\n'
        '业务码：00094\n'
        '单位：t \n'
        '单价：5000123456',
        '重量']
    assert target in dms









