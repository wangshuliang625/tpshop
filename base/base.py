import time
from selenium.webdriver.support.wait import WebDriverWait

from base.get_logger import GetLogger

log = GetLogger().get_logger()


class Base:

    def __init__(self, driver):
        log.info("[base]:正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("[base]:正在定位元素:{},默认超时时间为:{}".format(loc, timeout))
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素 方法封装
    def base_click(self, loc):
        log.info("[base]:正在对{}实行点击事件".format(loc))
        self.base_find(loc).click()

    # 输入元素 方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        log.info("[base]:正在对{}清空".format(el))
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息 方法封装
    def base_get_text(self, loc):
        log.info("[base]:正在对{}获取文本".format(loc))
        return self.base_find(loc).text

    # 截图 方法封装
    def base_get_image(self):
        log.info("[base]:断言出错,正在截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            log.info("[base]:{}元素查找成功,元素存在".format(loc))
            return True  # 代表元素存在
        except:
            log.info("[base]:{}元素查找失败,元素不存在".format(loc))
            return False  # 代表元素不存在

    # 回到首页

    # 切换frame表单

    # 回到默认目录方法
