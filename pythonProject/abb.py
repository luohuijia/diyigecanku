# # # from main import Count8
# from selenium import webdriver
# #from selenium.webdriver import ActionChains
# import time
# #web=webdriver.Chrome()
# # web.get('https://www.baidu.com/')
# # web.maximize_window()
# # #web.find_element_by_id('kw').send_keys('国美')
# # web.find_element_by_id('kw').send_keys('淘宝')
# #
# # time.sleep(2)
# # web.find_element_by_id('su').click()
# # time.sleep(2)
# # #web.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# # web.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# # #进入国美
# # add=web.window_handles
# # web.switch_to.window(add[-1])
# # #切换新窗口
# # #gm=web.find_elements_by_class_name("li.edit-mode.nav-item")
# # web.switch_to.frame(web.find_element_by_class_name('tbh-service J_Module'))
# # gm=web.find_elements_by_class_name("J_Cat.a-all")
# # time.sleep(2)
# # dz=ActionChains(web)
# # for el in gm:
# #     dz.move_to_element(el).perform()
# #     time.sleep(2)
#
# class fz():
#     def __init__(self):
#         self.web=webdriver.Chrome()
#
#     def dd(self):
#         self.web.implicitly_wait(3)
#
#     def dk(self,url):
#         self.web.get(url)
#         self.dd()
#
#     def shuru(self,aa,bb):
#         return self.web.find_element(aa,bb)
#
#     def __del__(self):
#         time.sleep(4)
#         self.web.close()
#
#
#
# # if __name__ == '__main__':
# #     a=fz()
# #     a.dk('https://www.baidu.com/')
# #     el=a.shuru('id','kw')
# #     el.send_keys('大司马')
# #     ela=a.shuru('id','su')
# #     ela.click()
#
#
#
#
#
#
from fengzhuang import Test2
import unittest
if __name__ == '__main__':
    unittest.main()

