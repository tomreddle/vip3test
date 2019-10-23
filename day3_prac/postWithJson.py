# 导入
import requests, json

# 方法一： 先导入json模块，用dumps方法将参数转化为json格式
# 接口地址
urlstr = 'http://www.kuaidi100.com/query'
# 参数
payload1 = {'type': 'shentong', 'postid': '1111111'}

# 使用 json.dumps方法将字符串转换成json格式
payload = json.dumps(payload1)

# 发送请求
r = requests.post(url=urlstr, data=payload)

# 获取结果
print(r.json())
print(r.text)
