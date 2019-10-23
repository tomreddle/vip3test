# 导入
import requests

# 接口地址
urlstr = 'http://v.juhe.cn/toutiao/index'
# 接口参数
payload = {'key': 'ca3943cc87485d7f940feea3bf7f23fb', 'type': 'shishang'}

# 发送请求
r = requests.post(url=urlstr, data=payload)

# 读取结果
print(r.json())
print(r.json()['result']['stat'])

# 1.第一种：application/json：这是最常见的json格式如下
# {"input1":"xxx","input2":"ooo","remember":false}
#  
# 2.第二种：application/x-www-form-urlencoded：浏览器的原生 form 表单，
# 如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数
# input1=xxx&input2=ooo&remember=false
#  
#
# 3.第三种：multipart/form-data:这一种是表单格式的，数据类型如下
#
# ------WebKitFormBoundaryrGKCBY7qhFd3TrwAContent-Disposition: form-data; name="text"
# title------WebKitFormBoundaryrGKCBY7qhFd3TrwAContent-Disposition:
# ------WebKitFormBoundaryrGKCBY7qhFd3TrwA--
#
# 4.第四种：text/xml:这种直接传的xml格式

