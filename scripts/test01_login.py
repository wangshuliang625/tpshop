# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 17:30 
# @Author : WSL
# @File : test01_login.py

import unittest
import time

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from parameterized import parameterized

from tool.read_txt import read_txt

log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))

    return arrs[1:]


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
            # 实例化PageLogin对象
            cls.login = PageLogin(GetDriver().get_driver())
            # 点击登录按钮
            cls.login.page_click_login_link()

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭driver驱动对象
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_result, status):
        try:
            # 调用登录业务方法
            self.login.page_login(username, pwd, verify_code)

            # 判断是否为正向用例
            if status == "ture":
                # 断言是否登录成功
                self.assertTrue(self.login.page_if_login_success())
                # 点击安全退出
                self.login.page_click_logout_link()
                # 点击登录链接
                self.login.page_click_login_link()
            # 逆向用例
            else:
                time.sleep(1)

                # 提示错误提示信息
                msg = self.login.page_get_erro_info()
                print("msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    log.error("错误:{}".format(e))
                    self.login.base_get_image()
            # 点击错误提示框确定按钮
            self.login.page_click_error_alert()

        except Exception as e:
            log.error("错误:{}".format(e))
