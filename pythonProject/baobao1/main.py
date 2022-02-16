from selenium import webdriver


class BasePage:
    # 构造方法
    def __init__(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()  # Alt+Enter
        # 加载百度首页
        self.driver.get('http://www.baidu.com')

    # 封装定位元素
    def find_ele(self, *args):
        ele = self.driver.find_element(*args)
        return ele