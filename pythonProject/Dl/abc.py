#
# import unittest
#
# from Dl import HTMLTestRunnerCN
#
# Lj = 'C:\\Users\\1\\PycharmProjects\\pythonProject'
#
# dis = unittest.defaultTestLoader.discover(Lj,'fengzhuang.py')
# # 定义报告存放路径
# filename = "C:\\Users\\1\\PycharmProjects\\pythonProject\\Dl\\result.htm"
# # 定义报告存放路径，如果没有，创建
# fp = open(filename, 'wb')
# # 定义测试报告
# runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
# # 运行测试用例
# runner.run(dis)
# # 关闭报告文件
# # fp.close()


#*****************************************************************************************

'''import requests
import json

url='http://localhost:8080/EasyBuy/Login'
data='loginName=admin&password=123456&action=login'

#req=requests.request('POST',url=url,params=data)
req=requests.post(url=url,params=data)
print(req.text)
#print(json.dumps(req.json(),indent=4, ensure_ascii=False))'''
import requests
import json
import jsonpath

#生成token接口
url = "http://localhost:8000/login"
# python 字典 --》 json
data = {
    "username": "admin",
    "password": "admin"
}
res = requests.post(url=url, json=data)
#使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
# 返回值是个列表 所以要加索引
# print(jsonpath.jsonpath(res.json(), "$..token")[0])

print("*************************************************************")

#登录jwt接口
urllogin = "http://localhost:8000/auth/hello"
#使用jsonpath来提取
token = "Bearer " + jsonpath.jsonpath(res.json(), "$..token")[0]
headers = {
    "Authorization":token
}
res1 = requests.get(url=urllogin,headers=headers)
print(json.dumps(res1.json(), indent=4, ensure_ascii=False))

print('************************************************************')

#上传文件接口
url = "http://httpbin.org/post"
# 准备一个文件
file = open("C:\\Users\1\\Desktop\\uhk.txt")
# 参数
files = {
    "file": file
}
res2 = requests.post(url=url, files=files)
#print(res.json())
print(json.dumps(res2.json(), indent=4, ensure_ascii=False))