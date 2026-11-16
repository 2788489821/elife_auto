# elife_auto — Web UI 自动化测试框架

基于 **Python + Selenium + pytest** 的 Web UI 自动化测试项目，采用 **POM（Page Object Model）** 分层设计，覆盖电商后台管理系统（SMP）的登录、设备类型、业务规则三个模块，共 **13 条用例**。

## 技术栈

| 类别 | 技术 |
|------|------|
| 语言 | Python 3.14 |
| UI 自动化 | Selenium 4.51 |
| 测试框架 | pytest 9.1 |
| 设计模式 | POM（BasePage + 页面类） |
| 等待策略 | 全程显式等待，无硬编码 sleep |

## 目录结构

```
elife_auto/
├── cfg.py                      # 环境配置（被测系统地址、各页面 URL）
├── conftest.py                 # fixture：driver 生命周期、登录前置、数据清理
├── lib/
│   └── base_page.py            # BasePage 基类：封装显式等待、通用元素操作
├── pages/                      # 页面对象层（元素定位 + 页面操作）
│   ├── login_page.py           # 登录页
│   ├── device_model_page.py    # 设备类型管理页
│   └── service_rule_page.py    # 业务规则管理页
└── cases/                      # 测试用例层（只写业务逻辑，不碰元素定位）
    ├── test_login.py           # 登录模块
    ├── test_device_model.py    # 设备类型模块
    └── test_service_rule.py    # 业务规则模块
```

## 被测系统

本地部署的电商后台管理系统（练习环境，来自白月黑羽软件测试教程），地址配置在 `cfg.py`：

```python
SMP_ADDRESS = 'http://127.0.0.1:8234/'
```

## 快速开始

```bash
# 1. 安装依赖
pip install selenium pytest

# 2. 启动被测系统（默认 127.0.0.1:8234）

# 3. 运行全部用例
pytest
```

> Selenium 4.6+ 自带 Selenium Manager，会自动匹配 Chrome 浏览器版本下载 driver，无需手动配置 chromedriver。

## 测试范围

| 模块 | 用例数 | 覆盖点 |
|------|--------|--------|
| 登录 | 7 | 正常登录；空用户名、空密码、错误密码、不存在用户等异常入参，校验提示文案 |
| 设备类型 | 2 | 新增、删除设备类型 |
| 业务规则 | 4 | 新增、删除、切换计费模式等操作 |
| **合计** | **13** | 全部通过 |

## 框架设计要点

- **POM 分层**：元素定位与页面操作封装在 `pages/` 页面类中，用例层只描述业务动作，页面改动只需改一处。
- **driver 生命周期管理**：`conftest.py` 中 module 级 fixture 管理 driver，同一模块用例共享浏览器实例，跑完自动 `quit()`。
- **登录前置统一处理**：`manager_page` fixture 参数化传入"页面类 + URL"，自动完成登录并跳转，用例直接拿到已登录的页面对象。
- **数据清理保证可重复执行**：新增的数据由后置 fixture 自动删除（`clean_one_record`、`close_add_form`、`clearAlert` 均有容错处理），重复运行不留脏数据。
- **显式等待**：所有元素操作前均使用显式等待（元素可见/可点击），用例稳定不抖动。
