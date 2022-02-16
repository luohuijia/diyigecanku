from ddt import ddt,data
from one import BaiduPage
import unittest
import time


@ddt
class BaiduTest(unittest.TestCase):

    @data('亚克托斯', '拉亚斯特')
    def test1(self, abb):
        BaiduPage().search(abb)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

    from ui_test import HTMLTestRunnerCN
    import unittest

    # 文件路径
    Testcase_dir = 'C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test'
    # 覆盖该文件路径下的文件
