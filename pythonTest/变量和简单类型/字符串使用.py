# 转义字符   \
# python 中的转义字符
# \b    退格符
# \n    换行符
# \r    回车符
# \t    制表符
# \'    单引号
# \"    双引号
# \\    反斜杠
# 示例换行
s = 'Hello\nCharlie\nGood\nMorning'
print(s)
# 示例制表符
s = '商品名\t\t\t单价\t\t数量\t\t总价'
s1 = '疯狂Java讲义\t108\t\t\t2\t\t\t216'
print(s, s1, sep='\n')


# 字符串格式化
# python支持使用 % 对各种类型进行格式化输出
# 示例
price = 108
print('price:%d' % price)

# 格式：
# 第一部分是格式化字符串（字符串模板），包含一个%d占位符，会被第三部分的变量或者表达式的值替代
# 第二部分是固定的 % 作为分隔符
# 第三部分对第一部分提供相应的值
# 占位符说明
# d,i   转换为带符号的十进制整数
# o     转换为带符号的八进制整数
# x     转换为带符号的十六进制整数
# X     转换为带符号的十六进制整数
# e     转换为科学计数法的浮点数，e小写
# E     转换为科学计数法的浮点数，E小写
# f,F   转换为十进制的浮点数
# g     智能选择f或者e格式
# G     智能选择F或者E格式
# C     转换为单字符（只接受整数或者单字符字符串）
# r     使用repr()将变量或表达式转换为字符串
# s     使用str()将变量或表达式转换为字符串

# 使用占位符时可以指定转换后的最小宽度，程序转换数值时，转换成的字符串总是右对齐的，宽度不够补空格
# 在至于小宽度之前添加标志
# -：左对齐
# +：表示数值总要带着符号
# 0：表示不补充空格，而是0
# 对于浮点数，允许指定小数点之后的位数
# 对于支付穿，允许设定字符串的最大字符数
# 示例
num = -28
print('num is: %6i' % num)
print('num is: %6d' % num)
print('num is: %6o' % num)
print('num is: %6x' % num)
print('num is: %6X' % num)
print('num is: %6s' % num)
print('num is: %06d' % num)     # 0补齐
print('num is: %+6s' % num)     # 带符号
print('num is: %-6s' % num)     # 左对齐
num1 = 3.14159265354
# 最小宽度是8，小数点后面3位
print('num is: %8.3f' % num1)
# 最小宽度是8，小数点后面3位，左边补0，带符号
print('num is: %+08.3f' % num1)

the_name = 'Charlie'
# 只保留三个字符
print('the name is : %.3s' % the_name)
# 只保留两个字符，最小宽度10，左对齐
print('the name is : %-10.2s' % the_name)

# 字符串可以使用列表的操作方法进行操作
s = 'crazyit.org is very good'
print(s[2])     # 第三个字符
print(s[-4])    # 倒数第四个字符
print(s[3:5])   # 从第四个到第六个字符的子字符串
print(s[3:-5])  # 从第四个到倒数第五个字符的子字符串
print(s[-6:-3])     # 从倒数第六个到倒数第三个字符的子字符串
print(s[:5])        # 从第一个到第六个字符的子字符串
print(s[:-6])       # 从第一个到倒数第六个字符的子字符串
print('very' in s)  # 判断‘very’是否在s中，返回boolean  True   False
print('fkit' in s)  # 判断‘very’是否在s中，返回boolean  True   False
print(len(s))       # 字符串的长度
print(len('test'))  # 字符串的长度
print(max(s))       # 字符串s的最大字符     z
print(min(s))       # 字符串s的最小字符   空格

# 大小写相关方法
print(dir(str))     # 查看str中的方法
help(str)           # 查看str的方法
# 关于str中与大小写的常用方法
# title()   把每个单词的首字母改为大写
# lower()   将整个字符串改为小写
# upper()   将整个字符串改为大写
a = 'our domain is crazingit.org'
# 每个单词的首字母大写
print(a.title())
print(a)
# 每个字母小写
print(a.lower())
# 每个字母大写
print(a.upper())

# 删除空白
# strip()   删除字符串前后的空白，如果指定参数则删除字符串前后的指定字符
# lstrip()  删除字符串前的空白，如果指定参数则删除字符串前的指定字符
# rstrip()  删除字符串后的空白，如果指定参数则删除字符串后的指定字符
s = '*sjsjs*'
print(s.strip('*'))

# 字符串的查找和替换方法
# startswitch()     判断字符串是否以指定字符（子串）开头
# endswith()        判断字符串是否以指定字符（子串）结尾
# find()            判断指定子串在字符串中出现的位置，如果没有指定字符串则返回-1
# index()           查找指定子串在字符串中出现的位置，如果没有找到指定子串，则会引发ValueError
# replace()         使用指定子串替换字符串中的目标子串
# translate()       使用指定的翻译映射映射表对字符串进行操作

s = 'crazyit.org is a good site'
# 判断s 是否以crazyit开头
print(s.startswith('crazyit'))
# 判断s 是否以site结尾
print(s.endswith('site'))
# 查找s中‘org’出现的位置
print(s.find('org'))
# 查找s中‘org’出现的位置
print(s.index('org'))
# 从索引9处开始查找‘org’出现的位置
print(s.find('org', 9))
# 从索引9处开始查找‘org’出现的位置
# print(s.index('org', 9))      # 从索引9 开始找不到org  报错  ValueError
# 将字符串中的所有it替换成xxxx
print(s.replace('org', 'xxxx'))
# 将字符串中的1个it替换成xxxx
print(s.replace('org', 'xxxx', 1))
# 定义翻译映射表：97  945  98  945 116 964
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))
# maketranes()  比较方便的创建翻译列表
table = str.maketrans('abt', 'αβγ')
print(table)

# 字符串的分割和连接
# split()
# join()
s = 'crazyit.org is a good site'
# 使用空白对字符串进行分割
print(s.split(' '))     # ['crazyit.org', 'is', 'a', 'good', 'site']
print(s.split())        # ['crazyit.org', 'is', 'a', 'good', 'site']
# 使用空白对字符串进行分割，最对分割前两个单词
print(s.split(' ', 2))      # ['crazyit.org', 'is', 'a good site']
print(s.split(None, 2))    # ['crazyit.org', 'is', 'a good site']
# 使用点进行分割
print(s.split('.'))         # ['crazyit', 'org is a good site']

mylist = s.split()
# 使用/将字符串进行连接
print('/'.join(mylist))
# 使用.将字符串进行连接
print('.'.join(mylist))

