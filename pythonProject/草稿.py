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

        from selenium import webdriver
        import unittest
        import time
        from selenium.webdriver.common.keys import Keys

        class Test(unittest.TestCase):

            def setUp(self):
                self.driver = webdriver.Chrome()
                self.driver.get("http://localhost:8080/EasyBuy")

            def test1(self):
                self.driver.find_element_by_xpath('//html/body/div[5]/div/ul/li[2]/a').click()
                time.sleep(3)
                # el=self.driver.find_element_by_xpath('//html/body/div[6]/div[1]/div[2]/div[2]/ul/li[1]/div[4]/a[1]')
                # self.assertTrue(el.is_enabled(),"收藏失败")

            # @unittest.skip('不执行此用例')
            def test2(self):
                self.driver.find_element_by_xpath('//html/body/div[4]/div[2]/form/input[1]').send_keys('香水', Keys.ENTER)

            def tearDown(self):
                time.sleep(5)
                self.driver.quit()

        # 方法一：
        if __name__ == '__main__':
            unittest.main()

        # 测试套可以放在if __name__ == '__main__'下执行也可以直接执行

        # 方法二：
        # 创建一个测试套件，并向其中加载测试用例
        # suite=unittest.TestLoader().loadTestsFromTestCase(Test)
        # 显式运行测试没并且通过设置verbosity设定对每一个测试方法产生测试结果；run中传入要执行的测试套件
        # unittest.TextTestRunner(verbosity=2).run(suite)

        # 方法三：
        # testunit = unittest.TestSuite()
        # testunit.addTest(Test("test2"))
        # unittest.TextTestRunner().run(testunit)


        from selenium import webdriver
        import unittest
        import time

        class Test(unittest.TestCase):
            # 在一个类中只会在所有测试用例运行前调用一次
            @classmethod
            def setUpClass(cls):
                cls.driver = webdriver.Chrome()
                cls.driver.get("http://www.baidu.com")
                cls.driver.maximize_window()

            # @unittest.skip('不执行此用例')
            def test1(self):
                self.driver.find_element_by_id('kw').send_keys('china')
                # self.driver.find_element_by_name('wd').send_keys('中国')
                self.driver.find_element_by_id('su').click()
                time.sleep(3)
                # 回退到上一步
                self.driver.back()
                time.sleep(3)

            def test2(self):
                # 获取‘新闻’的元素并打新闻页面
                self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
                # 暂停3秒
                time.sleep(3)
                # 获取所有窗口
                self.handles = self.driver.window_handles
                # 切换到新窗口
                self.driver.switch_to.window(self.handles[1])
                # 暂停3秒
                time.sleep(3)
                # 在新闻页面搜索‘国内新闻’
                self.driver.find_element_by_id('ww').send_keys('国内新闻')
                self.driver.find_element_by_id('s_btn_wr').click()

            # 在所有测试用例运行后调用一次
            @classmethod
            def tearDownClass(cls):
                time.sleep(5)
                cls.driver.quit()

        if __name__ == '__main__':
            unittest.main()

