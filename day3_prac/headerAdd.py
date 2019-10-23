# 导入
import requests

# urlstr = 'https://www.wanandroid.com/user/login'
urlstr = 'https://www.baidu.com/'
# header = {'Accept-Encoding': 'gzip,deflate'}
header = {}
# header = {'User-Agent': 'Mozilla/6.0'}
header['User-Agent'] = 'Mozilla/6.0'
header['Accept-Encoding'] = 'gzip,deflate'
# payload = {'username': 'chaoge', 'password': '123456'}
# header.keys['Accept-Encoding'] = 'gzip'

# 发送请求
# r = requests.post(url=urlstr, data=payload, headers=header)
r = requests.post(url=urlstr, headers=header)

# 获取结果
print(r.headers)

