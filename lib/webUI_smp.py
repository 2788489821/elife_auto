from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from cfg import *
from selenium.webdriver.support.ui import Select


class SMP_UI:
    def __init__(self, wd):
        self.wd = wd
        self.wd.implicitly_wait(10)
        self.wait = WebDriverWait(self.wd, 10)

    # 通过xpath路径获取元素
    def get_elem(self, xpath):
        elem = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return elem

    # 清空文本框并输入数据
    def input_text(self, xpath, text):
        ele = self.get_elem(xpath)
        ele.clear()
        ele.send_keys(text)

    # 点击元素
    def click_elem(self, xpath):
        self.get_elem(xpath).click()

    def login(self, username, password):
        # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
        self.wd.get(SMP_URL_LOGIN)
        time.sleep(1)
        if username is not None:
            self.input_text('//input[@id="username"]', username)
        if password is not None:
            self.input_text('//input[@id="password"]', password)
        time.sleep(1)
        self.click_elem('//button[@id="loginBtn"]')

    def get_first_page_device_models(self):
        time.sleep(1)
        self.wd.implicitly_wait(0)
        values = self.wd.find_elements(By.CSS_SELECTOR, '.field-value')
        self.wd.implicitly_wait(10)
        deviceModels = []
        for idx, value in enumerate(values):
            if (idx + 1) % 3 == 0:
                deviceModels.append(
                    [values[idx - 2].text, values[idx - 1].text, values[idx].text]
                )
        return deviceModels

    def get_first_page_service_rules(self):
        time.sleep(1)
        self.wd.implicitly_wait(0)
        values = self.wd.find_elements(By.CSS_SELECTOR, '.field-value')
        self.wd.implicitly_wait(10)
        serviceRules = []
        for idx, value in enumerate(values):
            if (idx + 1) % 4 == 0:
                serviceRules.append(
                    [values[idx - 3].text, values[idx - 2].text, values[idx - 1].text, values[idx].text]
                )
        return serviceRules

    def del_first_item(self) -> bool:
        self.wd.implicitly_wait(0)
        delBtn = self.wd.find_elements(By.CSS_SELECTOR, '.result-list-item:first-child .result-list-item-btn-bar span:first-child')
        self.wd.implicitly_wait(10)
        if not delBtn:  #
            return False
        delBtn[0].click()
        self.wd.switch_to.alert.accept()
        return True

    def add_device_model(self, devtype, name, desc):
        select = Select(self.wd.find_element(By.ID, 'device-type'))
        select.select_by_visible_text(devtype)

        self.input_text('//input[@id="device-model"]', name)
        self.input_text('//input[@id="device-model-desc"]', desc)
        self.wd.find_element(By.CSS_SELECTOR, '.add-one-submit-btn-div > span').click()

    def add_service_rule(self, name, rule_type, min_consume, estimate_consume, billing_unit, price_per, rule_desc, fee_list=None):
        if fee_list is None:
            fee_list = []
        # 规则名称
        self.input_text('//span[text()="规则名称"]/following-sibling::input', name)
        # 规则类型选择框
        select_ele = self.get_elem('//span[text()="规则类型"]/following-sibling::select')
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
            first_fee = fee_list[0]
            # 业务码
            self.input_text('//span[text()="业务码"]/following-sibling::input', first_fee[0])
            # 计费单位
            self.input_text('//span[text()="计费单位"]/following-sibling::input', first_fee[1])
            # 单价
            self.input_text('//span[text()="单位价格"]/following-sibling::input', first_fee[2])
            for one_fee in fee_list[1:]:
                self.click_elem('//span[text()="添加费率"]/following-sibling::input')
                time.sleep(1)
                entry = self.get_elem('div.fee-rate:last-child')
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(1)').send_keys(one_fee[0])
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(2)').send_keys(one_fee[1])
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(3)').send_keys(one_fee[2])
        # 规则描述
        self.input_text('//span[text()="规则描述"]/following-sibling::input', rule_desc)
        # 点击确定按钮
        self.click_elem('//div[@class="add-one-submit-btn-div"]/span')
