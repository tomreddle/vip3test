import requests
# 通过rquests.session自动设置cookie

urlstr = 'https://www.wanandroid.com/user/login'
data = {'username': 'chaoge', 'password': '123456'}

s = requests.session()
r = s.post(url=urlstr, data=data)

r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
print('****', r2.text)
print('****', r.text)
