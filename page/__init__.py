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

"""
以下为购物车模块涉及元素 配置信息
"""
# 搜索框
cart_search = By.CSS_SELECTOR, "#q"
# 搜索按钮
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 添加购物车 -->跳转到详情页面
cart_add_info = By.CSS_SELECTOR, ".p-btn>a"
# 添加购物车 -->
cart_add = By.CSS_SELECTOR, "#join_cart"
# iframe表单名称 name
cart_frame_name = "layui-layer-iframe1"
# id属性 定义元素
cart_frame_id = By.CSS_SELECTOR, "#layui-layer-iframe1"
# 获取添加购物车结果
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
# 关闭提示窗口
cart_close_window = By.CSS_SELECTOR, ".layui-layer-close"
