import requests

urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'chaoge', 'password': '123456'}

s = requests.session()

r = s.post(url=urlstr, data=payload)
# r = requests.post(url=urlstr, data=payload)
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0')

print('{}'.format(r2.text))
print('{}'.format(r.text))
