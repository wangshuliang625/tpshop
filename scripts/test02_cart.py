# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 9:03 
# @Author : WSL
# @File : test02_cart.py

import unittest

from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin


class TestCart(unittest.TestCase):

    # 定义setUp方法
    @classmethod
    def setUpClass(cls) -> None:
        # 获取driver对象
        cls.driver = GetDriver().get_driver()
        # 实例化PageCart页面
        cls.cart = PageCart(cls.driver)
        # 调用成功登录 依赖
        PageLogin(cls.driver).page_login_success()
        # 跳转到首页
        cls.cart.page_open_index()

    # 定义tearDown方法
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭driver对象
        GetDriver().quit_driver()

    # 定义购物车测试方法
    def test02_cart(self):
        # 调用组合添加购物车业务方法
        self.cart.page_add_cart()
        # 断言是否添加成功
        msg = self.cart.page_get_text()
        self.assertEqual(msg, "添加成功")
        # 关闭窗口
        self.cart.page_close_window()
