import time

from selenium.webdriver.common.by import By
from YUAN import Dl

class Sr(Dl):
    bai = (By.ID,"kw")
    du = (By.ID,'su')
    dz = (By.XPATH,'/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]')
    ad = (By.ID,'img_out_1505328345')
    def b(self):
        return self.ys(*Sr.bai)
    def c(self):
        return self.ys(*Sr.du)
    def d(self):
        return self.ys(*Sr.dz)
    # def e(self):
    #     return self.ys(*Sr.ad)

    # def aa(self):
    #     self.web.switch_to.window(all[-1])

    def qq(self,l):
        self.b().send_keys(l)
        self.c().click()
        time.sleep(2)
        self.d().click()





