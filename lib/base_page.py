from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, wd):
        self.wd = wd
        self.wait = WebDriverWait(self.wd,10)

    def input_text(self, xpath, text):

        ele = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        ele.clear()
        ele.send_keys(text)

    def click_elem(self, xpath):
        ele = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        ele.click()

    def get_text_elem(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_text_elems(self, xpath):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def get_alert(self):
        self.wait.until(EC.alert_is_present())
        return self.wd.switch_to.alert

    # def close_add_form(self):
    #     ele = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="取消"]')))
    #     ele.click()