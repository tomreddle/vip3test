# 导入resquests
import requests

# 地址参数
urlstr = 'http://v.juhe.cn/toutiao/index'
# 接口参数 类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐)
# tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
payload = {'key': 'ca3943cc87485d7f940feea3bf7f23fb', 'type': 'shishang'}

# 发送带参数的get请求
r = requests.get(url=urlstr, params=payload)

# 打印响应
print(r.text)
print(r.status_code)
