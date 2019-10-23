# 导入
import requests

# 第二种方法:使用json参数默认将参数处理成json传入post
# url
urlstr = 'http://httpbin.org/post'
# 接口参数
payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群号': '106014970'}
# header = {'Content-Type': 'application/json'}
# 发送请求
r = requests.post(url=urlstr, data=payload)

# 获取结果
print(r.json())
print(r.text)
print(r.content)
print(r.status_code)
