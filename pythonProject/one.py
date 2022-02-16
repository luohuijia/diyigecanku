from selenium.webdriver.common.by import By
from main import BasePage

class BaiduPage(BasePage):
        # 元素定位，
        baidu_text_loc = (By.ID, 'kw')
        baidu_submit_loc = (By.ID, 'su')

        # 获得元素对象，
        def get_text_obj(self):
            ele = self.find_ele(*BaiduPage.baidu_text_loc)
            return ele

        def get_submit_obj(self):
            ele = self.find_ele(*BaiduPage.baidu_submit_loc)
            return ele




        # 页面操作
        def search(self, a):
            self.get_text_obj().send_keys(a)
            self.get_submit_obj().click()

        #页面关闭
