import requests, re
# 通过定制cookie，放入header来访问目标网址
urlstr = 'https://www.wanandroid.com/user/login'
data = {'username': 'chaoge', 'password': '123456'}

r = requests.post(url=urlstr, data=data)
# print(r.text)
# print(r.cookies)
# print(r.headers)
print(r.cookies['JSESSIONID'])

header = {
    'cookie': 'JSESSIONID=' + r.cookies['JSESSIONID']
}
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0', headers=header)
# print(r2.text)
result = r2.text.find('已完成清单')
# print(result)
if result != -1:
    print('查询成功')
else:
    print('查询失败')

# 正则
# pattern = re.compile(r';\">(.*?)<\/h2>')
# result = pattern.findall(r2.text)
# print(result)
