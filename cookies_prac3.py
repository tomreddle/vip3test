import requests
# 通过定制cookie，单独设置cookie来访问目标网址

urlstr = 'https://www.wanandroid.com/user/login'
data = {'username': 'chaoge', 'password': '123456'}

r = requests.post(url=urlstr, data=data)
print('****', r.text)
print('****', r.cookies)

cookie = {
    'JSESSIONID': r.cookies['JSESSIONID']
}

r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0', cookies=cookie)
print(r2.text)
print(r2.headers)
