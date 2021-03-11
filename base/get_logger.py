# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 16:16 
# @Author : WSL
# @File : get_logger.py

import logging.handlers
import time



class GetLogger:

    logger = None
    @classmethod
    def get_logger(cls):
        # 如果logger为空
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器默认级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理文件
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/{}.log".format(time.strftime("%Y_%m_%d")),
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")

            # 获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器设置处理器中
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            # 将处理器添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        # 返回日志器
        return cls.logger
