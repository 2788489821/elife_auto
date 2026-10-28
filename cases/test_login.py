from selenium.webdriver.common.by import By
import time,pytest

def test_SMP_login_001(smpUI):
    smpUI.login('byhy','sdfsdf')

    time.sleep(1)
    nav = smpUI.wd.find_elements(By.TAG_NAME,'nav')

    assert nav !=[]

@pytest.fixture
def clearAlert(smpUI):
    yield
    try:
        smpUI.wd.switch_to.alert.accept()
    except Exception as e:
        print(e)

@pytest.mark.parametrize('username,password,expectedalert',[
    (None,'sdfsdf','请输入用户名'),
    ('byhy',None,'请输入密码'),
    ('byhy','sdfsdff','登录失败： 用户名或者密码错误'),
    ('byhy','sdfsd','登录失败： 用户名或者密码错误'),
    ('byhyy','sdfsdf','登录失败： 用户名不存在'),
    ('byh','sdfsdf','登录失败： 用户名不存在'),
])
def test_SMP_login_002(username,password,expectedalert,clearAlert,smpUI):
    smpUI.login(username, password)

    time.sleep(1)

    alert = smpUI.wd.switch_to.alert
    assert alert.text == expectedalert