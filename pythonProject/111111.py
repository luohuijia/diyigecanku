# import unittest
# import fengzhuang
# if __name__ == '__main__':
#  unittest.main(fengzhuang)
# import requests
# import json
#
# url='http://localhost:8080/EasyBuy/Login'
# data='loginName:admin&password=123456&action=login'
# req=requests.get(url=url,params=data)
# print(req.json())

#print(json.dumps(req.json(),indent=4, ensure_ascii=False))
#_________________________________________________________________
import requests
import json
import jsonpath

url ='http://localhost:8000/login'
data={
    'username':'admin',
    'password':'admin'

}

res= requests.post(url=url,json=data)

print(json.dumps(res.json(),indent=4,ensure_ascii=False))
# print(res.json())

print('-----------------------------------')
urll='http://localhost:8080/auth/hello'

token='Bearer'+jsonpath.jsonpath(res.json(),'$..token')[0]
headers={
    "Authorization":token
}
res1=requests.get(url=urll,headers=headers)

print(json.dumps(res1.json(),indent=4,ensure_ascii=False))


print('----------------------------------------------')
url2='http://hhtpbin.org/post'

file=open('C:\\Users\1\\Desktop\\uhk.txt','rb')

files={
    'file':file
}
res2=requests.post(url=url2,files=files)

print(json.dumps(res2.json(),indent=4,ensure_ascii=False))