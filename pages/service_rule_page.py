from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from lib.base_page import BasePage
from selenium.common import TimeoutException

class ServiceRulePage(BasePage):
    def get_first_page_service_rules(self):
        try:
            values = self.get_text_elems('//*[@class="field-value"]')
            serviceRules = []
            for idx, value in enumerate(values):
                if (idx + 1) % 4 == 0:
                    serviceRules.append(
                        [values[idx - 3].text, values[idx - 2].text, values[idx - 1].text, values[idx].text]
                    )
            return serviceRules
        except TimeoutException:
            return False

    def del_first_item(self) -> bool:
        try:
            self.click_elem('(//div[contains(@class,"result-list-item")])[1]//*[@class="btn-no-border"]')
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
            return True
        except TimeoutException:
            return False

    def add_service_rule(self, name, rule_type, min_consume, estimate_consume, billing_unit, price_per, rule_desc, fee_list=None):
        self.click_elem('//span[text()="添加"]')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"add-one-form")]')))

        if fee_list is None:
            fee_list = []
        # 规则名称
        self.input_text('//span[text()="规则名称"]/following-sibling::input', name)
        # 规则类型选择框
        select_ele = self.get_text_elem('//span[text()="规则类型"]/following-sibling::select')
        select = Select(select_ele)
        select.select_by_visible_text(rule_type)

        if rule_type in ["预付费-下发业务量", "预付费-下发费用"]:
            # 最小消费
            self.input_text('//span[text()="最小消费"]/following-sibling::input', min_consume)
            # 预估消费
            self.input_text('//span[text()="预估消费"]/following-sibling::input', estimate_consume)

        if rule_type == '预付费-下发业务量':
            # 计费单位
            self.input_text('//span[text()="计费单位"]/following-sibling::input', billing_unit)
            # 单价
            self.input_text('//span[text()="单位价格"]/following-sibling::input', price_per)

        if rule_type == '后付费-上报业务量':
            if not fee_list:
                raise ValueError("后付费-上报业务量传入至少一条费率 fee_list")
            first_fee = fee_list[0]
            # 业务码
            self.input_text('//span[text()="业务码"]/following-sibling::input', first_fee[0])
            # 计费单位
            self.input_text('//span[text()="计费单位"]/following-sibling::input', first_fee[1])
            # 单价
            self.input_text('//span[text()="单位价格"]/following-sibling::input', first_fee[2])
            for one_fee in fee_list[1:]:
                self.click_elem('(//div[contains(@class,"fee-rate")]//button[text()="添加费率"])[last()]')

                self.wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '(//div[contains(@class,"fee-rate")])[last()]')))

                row = '(//div[contains(@class,"fee-rate")])[last()]'
                self.input_text(f'{row}//input[1]', one_fee[0])
                self.input_text(f'{row}//input[2]', one_fee[1])
                self.input_text(f'{row}//input[3]', one_fee[2])
        # 规则描述
        self.input_text('//span[text()="规则描述"]/following-sibling::input', rule_desc)
        # 点击确定按钮
        self.click_elem('//div[@class="add-one-submit-btn-div"]/span')
