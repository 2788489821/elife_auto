import pytest
from pages.login_page import LoginPage

def test_SMP_login_001(driver):
    page = LoginPage(driver)
    page.login('byhy','sdfsdf')

    assert page.is_login_success()

@pytest.mark.parametrize('username,password,expectedalert',[
    (None,'sdfsdf','请输入用户名'),
    ('byhy',None,'请输入密码'),
    ('byhy','sdfsdff','登录失败： 用户名或者密码错误'),
    ('byhy','sdfsd','登录失败： 用户名或者密码错误'),
    ('byhyy','sdfsdf','登录失败： 用户名不存在'),
    ('byh','sdfsdf','登录失败： 用户名不存在'),
])
def test_SMP_login_002(username, password, expectedalert, clearAlert, driver):
    page = LoginPage(driver)
    page.login(username, password)

    assert page.get_alert_text() == expectedalert