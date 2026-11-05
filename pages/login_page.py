from lib.base_page import BasePage
from cfg import *
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def login(self, username, password):
        # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
        self.wd.get(SMP_URL_LOGIN)
        if username is not None:
            self.input_text('//input[@id="username"]', username)
        if password is not None:
            self.input_text('//input[@id="password"]', password)
        self.click_elem('//button[@id="loginBtn"]')

    def is_login_success(self):
        return len(self.wd.find_elements(By.TAG_NAME, 'nav')) > 0

    def get_alert_text(self):
        return self.get_alert().text