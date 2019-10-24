# 导入re
import re

# 使用re.split()分割
with open(r'C:\Users\hyr\Desktop\learning\第三天\abc.txt', 'r') as f:
    for i in f.readlines():
        line = re.split('\s\s\s\s+', i.strip())
        print(line)


str1 = 'Is is the cost of of gasoline going up up'
patt1 = re.match('^[A-Z]+', str1).group()
print(patt1)
