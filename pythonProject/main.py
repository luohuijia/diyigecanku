# #s="012345678"
# #a=s[3:0:-1]
# #print(a)
# '''a=[1,3,4,5,7,10,9]
#
# a.append(15)
# print(a)
#
# a.remove(3)
# print(a)'''
# #array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
#
# #i 表示第几轮“冒泡”(对比的轮数是实际的长度-1)
# # for i in range(1, len(array)):
# #     #j 表示“走访”到的元素索引，每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置
# #         for j in range(0, len(array) - i):
# #             #列表中第j个元素大于第j+1个元素
# #             if array[j] > array[j + 1]:
# #                 #升序
# #                 array[j], array[j + 1] = array[j + 1], array[j]
# # print(array)
#
# # dict1 = {'1':3}
# # dict2={'asda':"das"}
# # dict3=dict(dict2,**dict1)
# # print(dict3)
#
#
# # dict={}
# # dict['one'] = "This is one"
# # dict[2] = "This is two"
# #
# # print(dict)
# #tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
#
#
# #print (dict['one'])          # 输出键为'one' 的值
# #print (dict[2])              # 输出键为 2 的值
# #print (tinydict)             # 输出完整的字典
# #print (tinydict.keys())      # 输出所有键
# #print (tinydict.values())    # 输出所有值
# # import random
# # a = 1
# # b = 99
# # key = random.randint(1, 100)
# #
# # while 1:
# #     guess = int(input("请输入一个整数%d" % a + "到%d:" % b))
# #     if guess<key and guess > a:
# #         a = guess
# #         print('请输入%d到' % a+"到%d:" % b)
# #     elif guess>key and guess<b:
# #         b = guess
# #         print('请输入%d' % a+"到%d:" % b)
# #     elif guess <= 1 or guess >= 100:
# #         print("小伙子，别调皮，请重新输入")
# #     elif guess == key:
# #         print('真聪明，猜对了！')
# #         break
# # s = 0
# # i = 1
# # while i < 7:
# #     if i>0:
# #         s = s+i
# #     # else:
# #     #     pass
# #     i=2+i
# # d=9
# #     print(s)
# # class Count8():
# #     def add(self, a, b):
# #         return a+b
# #
# #     def acc(self, a, b):
# #         return a-b
# #
# #     def aff(self, a, b):
# #         # 这里的self就是类本身的实例参数
# #         return self.add(a, b)*self.acc(a, b)
#
# #两个函数返回的值相乘，得到的乘积结果返回给调用count函数的地方
#
# # 这里的a是外部的实例参数
# # a= Count8()  # 实例化
# # #调用了Count类中的aff方法，aff方法返回另外两个方法的相乘的结果，同时打印代码中的两个整数赋值给了方法中对应的a,b；例如打印代码中的3赋值给a，1赋值给b
# # print (Count8() .aff(3,1))
from selenium import webdriver
from selenium.webdriver import ActionChains


import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#最大化窗口
driver.maximize_window()
time.sleep(1)
#输入QQ邮箱后点击搜索
driver.find_element_by_id("kw").send_keys('QQ邮箱')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[2]/input').click()
time.sleep(2)
#点击第一个搜索结果标签
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]').click()
#切换到最新标签
abb=driver.window_handles
driver.switch_to.window(abb[-1])
#点击头像登录
time.sleep(2)
driver.switch_to.frame('login_frame')
time.sleep(2)
driver.find_element_by_id('img_out_1870564096').click()
time.sleep(4)
#登录成功
time.sleep(3)
#点击写信
driver.find_element_by_id('composebtn').click()
time.sleep(3)
driver.switch_to.frame('mainFrame')
time.sleep(2)
driver.find_element_by_id('subject').send_keys('关于二十多岁还不会火之呼吸')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1505328345@qq.com')
driver.find_element_by_xpath("//input[@type = 'file']").send_keys("C:\\JK\\666.txt")

driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea"]'))
driver.find_element_by_xpath('/html/body').send_keys('铁废物')
time.sleep(2)
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element_by_name('sendbtn').click()
#
# #driver.close()
# dian=ActionChains(driver)
# d=driver.find_element_by_id('lg')
# dian.context_click(d).perform()



