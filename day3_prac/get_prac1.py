# 导入requests模块
import requests

# 发送get请求
# 初始化url参数
urlstr = 'https://www.baidu.com/ '
# urlstr = 'https://www.baidu.com/ '
# 发送请求
r = requests.get(url=urlstr)

# 打印响应
# 字符串格式的响应体，并会根据响应头的编码格式自动解码 可能会乱码
print(r.text)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 响应状态码
print(r.status_code)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 字节方式的响应体，自动解码gzip和defalte压缩
print(r.content)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# Json格式的响应体,需注意，如响应体重没有json串会报错
# print(r.json())
# 获取url
print(r.url)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 获取编码格式
print(r.encoding)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 获取响应中返回的cookie
print(r.cookies)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 返回原始响应体
print(r.raw)
