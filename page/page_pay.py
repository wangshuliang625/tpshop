# -*- coding: utf-8 -*- 
# @Time : 2021/3/11 11:24 
# @Author : WSL
# @File : page_pay.py
from base.base import Base
import page


class PagePay(Base):
    # 点击我的订单链接
    def page_click_my_order_link(self):
        self.base_click(page.pay_my_order)

    # 点击立即支付
    def page_click_now_payment(self):
        # 必须先切换从窗口
        self.base_switch_to_window(page.pay_my_order_title)
        self.base_click(page.pay_now_payment)

    # 点击货到付款
    def page_click_pay_on_delivery(self):
        # 先切换窗口
        self.base_switch_to_window(page.pay_payment_title)
        self.base_click(page.pay_on_delivery)

    # 确认支付方式
    def page_click_payment_mode(self):
        self.base_click(page.pay_confirm_payment)

    # 获取支付结果
    def page_get_payment_result(self):
        return self.base_get_text(page.pay_payment_result)

    # 组合业务方法
    def page_pay(self):
        self.page_click_my_order_link()
        self.page_click_now_payment()
        self.page_click_pay_on_delivery()
        self.page_click_payment_mode()
