# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 10:51 
# @Author : WSL
# @File : get_driver.py

from selenium import webdriver
from page import URL


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取driver
            cls.driver = webdriver.Chrome()
            # 窗口最大化
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(URL)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()

            cls.driver = None
