# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 11:01 
# @Author : WSL
# @File : page_order.py
from time import sleep

import page
from base.base import Base


class PageOrder(Base):
    # 打开首页
    def page_click_index(self):
        self.base_index()

    # 点击我的购物车
    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)

    # 点击全选复选框
    def page_click_all_select(self):
        if not self.base_find(page.order_all).is_selected():
            self.base_click(page.order_all)

    # 点击去结算
    def page_click_account(self):
        self.base_click(page.order_account)

    # 备用 查找收货人
    def page_find_person(self):
        self.base_find(page.order_person)

    # 点击提交订单
    def page_click_submit_order(self):
        self.base_click(page.order_submit)

    # 获取订单提交结果
    def page_get_submit_result(self):
        return self.base_get_text(page.order_submit_result)

    # 组装订单业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_click_account()
        sleep(5)
        self.page_find_person()
        self.page_click_submit_order()
