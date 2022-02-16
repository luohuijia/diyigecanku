from selenium.webdriver.common.by import By
from baobao1.main import BasePage

class BaiduPage(BasePage):
        # 元素定位，
        bai = (By.ID, 'kw')
        du = (By.ID, 'su')

        # 获得元素对象，
        def b(self):
            ele = self.find_ele(*BaiduPage.bai)
            return ele

        def d(self):
            ele = self.find_ele(*BaiduPage.du)
            return ele

        # 页面操作
        def search(self, a):
            self.b().send_keys(a)
            self.d().click()



        #页面关闭
