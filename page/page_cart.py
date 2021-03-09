# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 16:48 
# @Author : WSL
# @File : page_cart.py
from base.base import Base


class PageCart(Base):

    # 打开首页
    def page_open_index(self):
        pass

    # 输入搜索内容
    def page_input_search(self):
        pass

    # 点击搜索按钮
    def page_click_search_btn(self):
        pass

    # 点击添加购物车 跳转到商品详情页
    def page_click_add_cart_info(self):
        pass

    # 点击添加购物车
    def page_click_add_cart(self):
        pass

    # 获取添加结果
    def page_get_text(self):
        pass

    # 关闭窗口
    def page_close_window(self):
        pass

    # 组合业务调用方法
    def page_add_cart(self):
        self.page_input_search()
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()
