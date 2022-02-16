from ddt import ddt, data
from one import BaiduPage
import unittest
import time


@ddt
class BaiduTest(unittest.TestCase):

    @data('软件测试', '硬件测试')
    def test01(self, abb):
        BaiduPage().search(abb)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()