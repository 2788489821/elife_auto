from pages.service_rule_page import ServiceRulePage


def test_SMP_Service_Rule_001(inServiceRuleManager, delAddedServiceModel, driver):
    page = ServiceRulePage(driver)
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











