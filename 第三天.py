import requests

# http://suggest.taobao.com/sug?code=utf-8&q=商品关键字&callback=cb
# urlstr = 'https://blog.csdn.net/rainshine1190'
# urlstr1 = 'https://www.wanandroid.com/article/query'
# urlstr2 = 'https://www.baidu.com'
urlstr = 'http://suggest.taobao.com/sug'
# 参数变量约定为payload
# payload = {'k': 'Android'}
r = requests.get(url=urlstr)
# 发送请求
# r = requests.get(url=urlstr1, params=payload)
# r = requests.get(url=urlstr2)
# print(r.text)   # 字符串方式的响应体
# print(r.content)    # 字节方式的响应体，自动解码gzip和deflate
# print(r.headers)
# print(r.status_code)
# 返回的是json才可以解析
s = r.json()
# print(r.url)
# print(r.encoding)
# print(r.cookies)
# print(r.raw)
# print(r.raise_for_status())
