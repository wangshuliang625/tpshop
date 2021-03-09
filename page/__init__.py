# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 16:32 
# @Author : WSL
# @File : __init__.py
"""
以下为项目地址
"""
URL = "http://localhost"

"""
以下为登录模块涉及元素 配置信息
"""
from selenium.webdriver.common.by import By

# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 错误提示信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"

# 错误提示框 确定按钮
login_err_ok_btn = By.CSS_SELECTOR, ".layui-layer-btn0"

# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"
