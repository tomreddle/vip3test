# 导入
import requests

# 接口地址
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'chaoge', 'password': '123456'}

# 发起请求
r = requests.post(url=urlstr, data=payload)

# 获取结果
print(r.text)
# 判断是否登录成功
if r.json()['data']['username'] == payload['username']:
    print('登录成功')
else:
    print('登陆失败')
# if r.text.find() != -1:
#     print('登录成功')
# else:
#     print('登陆失败')
# 使用正则表达式判断是否登录成功

