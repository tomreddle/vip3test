# 导入
import requests

# 接口地址
urlstr = 'http://www.kuaidi100.com/query'
# 参数设定
payload = {'type': 'shentong', 'postid': '1111111'}
# data = {'': '', '': ''}
# 发送请求
r = requests.get(url=urlstr, params=payload)
# 打印json格式响应
print(r.json())
print(r.text)