# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 14:49 
# @Author : WSL
# @File : test03_order.py

import unittest

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_order import PageOrder


log = GetLogger().get_logger()
class TestOrder(unittest.TestCase):

    # 定义setUp方法
    def setUp(self) -> None:
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 调用登录PageLogin对象中登录方法
        PageLogin(self.driver).page_login_success()
        # 实例化PageOrder
        self.order = PageOrder(self.driver)
        # 回到首页
        self.order.page_click_index()

    # 定义tearDown方法
    def tearDown(self) -> None:
        GetDriver().quit_driver()

    # 定义订单测试方法
    def test_order(self):
        try:
            # 调用下订单业务方法
            self.order.page_order()
            # 断言
            msg = self.order.page_get_submit_result()
            print(msg)
            self.assertIn("提交成功", msg)
        except Exception as e:
            # 截图
            self.order.base_get_image()
            print(e)
            log.error(e)
