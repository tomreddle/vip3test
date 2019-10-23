import requests, json

urlstr = 'http://httpbin.org/post'
payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群号': '106014970'}

r = requests.post(url=urlstr, json=payload)

# print(r.text)
print(r.json())
