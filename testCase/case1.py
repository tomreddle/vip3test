from common.readExcel import *
from common.configHttp import *
# from common import configHttp
# import json

path = '../dataFile'
file_name = 'data1.xlsx'
read_excel = Readexcel(path, file_name)
param1 = read_excel.tatol()
# print(param1)

for i in param1:
    interface_case = Confighttp(i[1] + '//' + i[2], i[3], i[5], eval(i[4]))
    r = interface_case.dorequest()
    print(r.text)
# str1 = "{'code':'utf-8','q':'python','callback':'cb'}"
# print(type(eval(str1)))

