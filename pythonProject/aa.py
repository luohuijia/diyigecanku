from selenium import  webdriver
import time
import xlrd

web=webdriver.Chrome()
web.maximize_window()

xls = xlrd.open_workbook("C:\\Users\\1\\Desktop\\baidu.xls")

a=xls.sheet_by_name('Sheet1')

list=[]

for b in range(0,a.nrows):
    list =a.row_values(b)
    break
print(list)
web.get(list[0])
time.sleep(2)

web.find_element_by_class_name(list[2]).send_keys(list[4])
time.sleep(2)

web.find_element_by_class_name(list[3]).click()
time.sleep(2)

all=web.window_handles
web.switch_to.window(all[-1])

web.find_element_by_xpath(list[5]).click()
time.sleep(3)

list2=[]


for c in range(1,a.nrows):
    list2 = a.row_values(c)
    break

web.find_element_by_class_name(list2[0]).click()
web.close()


