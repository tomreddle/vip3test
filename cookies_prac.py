import requests
# 通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie
urlstr = 'https://www.wanandroid.com/user/login'
data = {'username': 'chaoge', 'password': '123456'}

r = requests.post(url=urlstr, data=data)
print('***', r.text)
print('***', r.cookies)
print('***', r.headers)

cookie = r.cookies
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0', cookies=cookie)
if r.text.find('已完成'):
    print('******', r2.text, r2.status_code)
