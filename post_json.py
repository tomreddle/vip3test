import requests, json

urlstr = 'http://httpbin.org/post'
payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群号': '106014970'}
payload = json.dumps(payload)

r = requests.post(url=urlstr, data=payload)
print(r.status_code)
print(r.text)
print(r.json())
