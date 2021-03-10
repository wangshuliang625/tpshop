# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 16:07 
# @Author : WSL
# @File : page_login.py
from base.base import Base
import page
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        log.info("[page_login]:点击登录链接")
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        log.info("[page_login]:输入的用户名是:{}".format(username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("[page_login]:输入的密码是:{}".format(pwd))
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        log.info("[page_login]:输入的验证码是:{}".format(code))
        self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        log.info("[page_login]:点击登录按钮")
        self.base_click(page.login_btn)

    # 获取错误提示信息
    def page_get_erro_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击错误提示框 确定按钮
    def page_click_error_alert(self):
        self.base_click(page.login_err_ok_btn)

    # 判断是否登录成功
    def page_if_login_success(self):
        return self.base_element_is_exist(page.login_link)

    # 点击安全退出
    def page_click_logout_link(self):
        self.base_click(page.login_logout)

    # 判断是否退出成功
    def page_if_logout_success(self):
        return self.base_element_is_exist(page.login_link)

    # 组合业务方法-->登录业务直接调用
    def page_login(self, username, pwd, verify_code):
        log.info("[page_loging] 正在执行登录操作, 用户名：{} 密码：{}, 验证码:{}".format(username, pwd, verify_code))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()

    # 组合登录业务方法 给(购物车模块、订单模块、支付模块)依赖登录使用
    def page_login_success(self, username="13121134105", pwd="123456", verify_code="8888"):
        # 点击登录连接
        self.page_click_login_link()
        log.info("[page_loging] 正在执行登录操作, 用户名：{} 密码：{}, 验证码:{}".format(username, pwd, verify_code))
        # 调用 输入用户名
        self.page_input_username(username)
        # 调用 输入密码
        self.page_input_pwd(pwd)
        # 调用 输入验证码
        self.page_input_verify_code(verify_code)
        # 调用 点击登录
        self.page_click_login_btn()