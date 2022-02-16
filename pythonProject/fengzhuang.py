from selenium import webdriver
import time

# from abb import fz
# if __name__ == '__main__':
#     a=fz()
#     a.dk('https://www.baidu.com/')
#     el=a.shuru('id','kw')
#     el.send_keys('大司马')
#     ela=a.shuru('id','su')
#     ela.click()

# from selenium import webdriver
# import unittest
# import time
# class Test1(unittest.TestCase):
#     @classmethod
#     def
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('头柱')
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        # el=self.driver.find_element_by_xpath('//html/body/div[6]/div[1]/div[2]/div[2]/ul/li[1]/div[4]/a[1]')
        # self.assertTrue(el.is_enabled(),"收藏失败")

    #@unittest.skip('不执行此用例')
    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('猪突猛进')
        self.driver.find_element_by_id('su').click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

class Test2(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('头')
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        # el=self.driver.find_element_by_xpath('//html/body/div[6]/div[1]/div[2]/div[2]/ul/li[1]/div[4]/a[1]')
        # self.assertTrue(el.is_enabled(),"收藏失败")

    #@unittest.skip('不执行此用例')
    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('猪')
        self.driver.find_element_by_id('su').click()

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()
if __name__ == '__main__':
 unittest.main()