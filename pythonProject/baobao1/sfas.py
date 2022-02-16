#coding:utf-8
from selenium import  webdriver
import unittest
import  time

class test(unittest.TestCase):
    def testduanyan(self):
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        #等待3秒
        time.sleep(3)
        #在搜索框输入china
        self.driver.find_element_by_id("kw").send_keys("china")
        time.sleep(3)
        #点击搜索按钮
        self.driver.find_element_by_id("su").click()
        time.sleep(10)
        #断言（断言是unittest自带的方法，必需与unittest一起用）
        #self.assertEqual(self.driver.find_element_by_xpath('//*[@id="su"]').get_attribute("value"),u'百度一下',"百度失败")

        #判断bool值为True或为False
        #self.assertTrue(self.driver.find_element_by_xpath('//*[@id="su"]').is_enabled())

        #检查某个元素是否存在,当元素存在则pass
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="su"]'))
        time.sleep(5)
        #退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()