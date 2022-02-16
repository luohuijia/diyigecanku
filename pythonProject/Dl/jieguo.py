import time
import unittest
from ddt import ddt,data
from demo1 import Sr
from Dl import HTMLTestRunnerCN

@ddt
class jieguo(unittest.TestCase):
    @data('QQ邮箱')
    def test1(self,s):
        Sr().qq(s)
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()
# Lj='C:\Users\1\PycharmProjects\pythonProject\Dl'
#
# dis = unittest.defaultTestLoader.discover(Lj, 'jiegu.py')
# # 定义报告存放路径
# filename = "C:\JK"
# # 定义报告存放路径，如果没有，创建
# fp = open(filename, 'wb')
# # 定义测试报告
# runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
# # 运行测试用例
# runner.run(dis)
#         # 关闭报告文件
#         # fp.close()