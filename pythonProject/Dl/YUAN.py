from selenium import webdriver


class Dl:
    def __init__(self):
        self.web=webdriver.Chrome()
        self.web.get('https://www.baidu.com')
        self.web.maximize_window()
        #self.all=webdriver.Chrome().window_handles

    def ys(self,*y):
      aba= self.web.find_element(*y)
      return aba
