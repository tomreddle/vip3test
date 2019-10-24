# 导入re模块
import re

# match()     尝试正则表达式模式从字符串的开头匹配，如果匹配成功了，则返回匹配对象，否则返回None
# search()    在字符串中查找正则表达式模式第一次出现，如果匹配成功，则返回匹配对象，否则返回None
# findall()   在字符串中查找正则表达式的所有（非重复）出现，返回匹配对象列表
# split()     根据正则表达式中的分隔符把字符串分割成一个列表，返回成功匹配的列表，可以设定次数（默认分割所有匹配的地方）
# sub()       把字符串中所有匹配正则表达式的地方替换成字符串，如果次数没有给定，则替换所有匹配的地方
# group()     返回所有匹配对象或是根据要求返回某个特定子组（或指定编号是num的子组）

str1 = '123abcd123a'
# match 函数从开头检查是否字符串是否匹配正则表达式，有则返回匹配对象
print(re.match('123a', str1))           # 返回<re.Match object; span=(0, 4), match='123a'>

# print(re.match('23a', str1))            # 返回None
# search() 从字符串首次出现的位置开始匹配
print(re.search('23a', str1))           # 返回<re.Match object; span=(1, 4), match='23a'>
print(re.search('123a', str1))          # 返回<re.Match object; span=(0, 4), match='123a'>
print(re.search('1xy', str1))           # 返回None

# 匹配多个字符串
bt = 'bat|bet|bit'
print(re.match(bt, 'bat'))              # 返回<re.Match object; span=(0, 3), match='bat'>
print(re.match(bt, 'blt'))              # 返回None
print(re.match(bt, 'He bits me!'))      # 返回None
print(re.search(bt, 'He bits me!').group())     # 返回bit

# 匹配任意单个字符串 其中.表示出\n之外的任意一个变量
anyend = '.end'
print(re.match(anyend, 'bend'))         # 返回<re.Match object; span=(0, 4), match='bend'>
print(re.match(anyend, 'end'))          # 返回None
print(re.match(anyend, ' end'))          # 返回None
print(re.match(anyend, '\nend'))        # 返回None
print(re.search(anyend, 'Theend'))       # 返回<re.Match object; span=(2, 6), match='eend'>

# 创建字符集合（使用[ ]）
print(re.match('[cr][23][dp][o2]', 'c3po')) # <re.Match object; span=(0, 4), match='c3po'>
print(re.match('[cr][23][dp][o2]', 'c2do')) # <re.Match object; span=(0, 4), match='c2do'>
print(re.match('r2d2|c3po', 'c2do'))        # 返回None
print(re.match('r2d2|c3po', 'r2d2'))        # <re.Match object; span=(0, 4), match='r2d2'>

# 子组 使用( )   group()     返回所有匹配对象或是根据要求返回某个特定子组（或指定编号是num的子组）
w = '\w\w\w-\d\d\d'
w1 = '(\w\w\w)-(\d\d\d)'
print(re.match(w, 'abc-123').group())       # 返回abc-123
print(re.match(w1, 'abc-123').group())      # 返回abc-123
print(re.match(w1, 'abc-123').group(1))     # 返回abc
print(re.match(w1, 'abc-123').group(2))     # 返回123
print(re.match(w1, 'abc-123').groups())     # 返回('abc', '123')

# 从字符串的开头、结尾、单词的边界匹配
print(re.match('^The', 'The end.').group())        # 返回 The
print(re.match('^The', 'end The'))                  # 返回None
print(re.search('\\bthe', 'bite the dog').group())  # 返回 the  不转义的话会匹配不上
print(re.search(r'\bthe', 'bitethe dog'))     # 返回None
print(re.search(r'\Bthe', 'bite the dog'))      # 返回None

# findall(rule, target[,flag])
# flags包括:
# re.I  忽略大小写
# re.L  表示特殊字符集，\w \W \b \B \s \S，依赖当前环境
# re.M  多行模式
# re.S  '.'并且包括换行符在内的任意字符（即 . + \n）
# re.U  表示特殊字符集，\w \W \b \B \s \S，依赖Unicode字符属性数据库

html = '''
<html>
    <head>
        <title>这是一个标题</title>
        <title>这是一个标题1</title>
    </head>
    <body>
        <div class="topic"><a href="https://www.baidu.com">
            <div class="list">
                <ul>
                    <li><a href="http://www.filder.com">
                </ul>
            </div>
        </div>
    </body>
</html>
'''
title = re.findall('<title>(.*?)</title>', html)
print(title)
print(''.join(title))

links = re.findall('href="(.*?)"', html)
print(links)
# for i in links:
#     print(i)

# sun() 和subn() 搜索和替换
print(re.sub('X', 'Mr.Smith', 'attn:X\n\nDear X, \n'))
print(re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X, \n'))   # 返回替换次数


# print(re.search('\bthe', 'thebite the dog').group())

pattern = re.compile(r'\d+')
m = pattern.match('ab1233')
print(m)

print(pattern.match('ab1233', 2,))
