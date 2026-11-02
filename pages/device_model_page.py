from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from lib.base_page import BasePage


class DeviceModelPage(BasePage):
    def get_first_page_device_models(self):
        values = self.get_text_elems('//*[@class="field-value"]')
        deviceModels = []
        for idx, value in enumerate(values):
            if (idx + 1) % 3 == 0:
                deviceModels.append(
                    [values[idx - 2].text, values[idx - 1].text, values[idx].text]
                )
        return deviceModels

    def del_first_item(self) -> bool:
        self.click_elem('(//div[contains(@class,"result-list-item")])[1]//*[@class="btn-no-border"]')

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        return True

    def add_device_model(self, devtype, name, desc):
        self.click_elem('//span[text()="添加"]')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"add-one-form")]')))

        select_ele = self.get_text_elem('//select[@id="device-type"]')
        select = Select(select_ele)
        select.select_by_visible_text(devtype)

        self.input_text('//input[@id="device-model"]', name)
        self.input_text('//input[@id="device-model-desc"]', desc)
        self.click_elem('//div[@class="add-one-submit-btn-div"]/span')

