import requests

urlstr = 'https://www.wanandroid.com/user/login'
header = {'User-Agent': 'Mozilla/6.0'}
payload = {'username': 'chaoge', 'password': '123456'}

r = requests.post(url=urlstr, data=payload, headers=header)

print(r.text)
print(type(r.text))
# print(r.header)
print(type(r.json()))
print(r.json())
print(r.json()['data']['username'])

if r.json()['data']['username'] == payload['username']:
    print('登录成功')
if r.json()['data']['admin']:
    print('管理员')
else:
    print('不是管理员')
