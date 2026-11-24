# test_login.py
import pytest
import yaml
from pathlib import Path
from pages.login_page import LoginPage

# 加载yaml数据函数
DATA_PATH = Path(__file__).parent / "data" / "login_cases.yaml"
def load_login_cases():
    with open(DATA_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

def test_SMP_login_001(driver):
    page = LoginPage(driver)
    page.login('byhy','sdfsdf')
    assert page.is_login_success()

# 数据驱动：直接读yaml返回的case列表
@pytest.mark.parametrize("case", load_login_cases(), ids=lambda c: c["case_id"])
def test_SMP_login_002(case, clearAlert, driver):
    page = LoginPage(driver)
    username = case["username"]
    password = case["password"]
    expectedalert = case["expectedalert"]

    page.login(username, password)
    assert page.get_alert_text() == expectedalert
