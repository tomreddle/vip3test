# 导入
import requests,re

# user_agent = 'Mozilla/6.0'

# for i in range(1, 4):
urlstr = 'http://www.lovehhy.net/Joke/Detail/QSBK/' # + str(i)
r = requests.get(url=urlstr)
html = r.text

# 使用正则表达式来获取想要的内容
pick_url = re.findall('<div id="endtext">(.*?)</div>', html, re.S)
print(pick_url)
for j in pick_url:
    print(j.replace('<br/>', ''))
else:
    print('抓取成功')
