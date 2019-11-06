# 字符串：几乎包含所有字符，英文、中文、字母、数字等
# python中字符串可以使用单引号包裹，也可以使用双引号包裹，'abc'和"abc"都可以
# 如果字符串中本身就有单引号或双引号，则需要使用双引号或单引号进行包裹，或者进行转义
print("this's a example")       # this's a example
print('this is a "example"')    # this is a "example"
print("this is a \"example\"")  # this is a "example"


# 如果将两个字符紧挨着写在一起，python会自动进行拼接,成为元组
a1 = "Hello", 'World'
print(a1)               # ('Hello', 'World')
print(type(a1))         # <class 'tuple'>
# 如果想拼接字符串可以使用字符串 拼接运算符‘+’
a2 = 'hello '
a3 = 'everyone'
a4 = a2 + a3
print(a4)               # hello everyone

# repr和字符串
# python不允许字符串和数值进行拼接，必须先进行转换
# str() 或 repr()
# str() 是python 的内置函数，可以对象转换为字符串格式
# repr() 是以表达式的形式来表示
st = 'We will rick you'
print(st)           # We will rick you
print(str(st))      # We will rick you
print(repr(st))    # 'We will rick you'

# input()向用户生成一跳提示，然后获取用户输入的内容，返回一个字符串
msg = input('请输入：')  # 请输入：
print(type(msg))        # <class 'str'>
print(msg)              # 打印输入的内容

# 长字符串
# 使用三个引号（单引号或双引号）   就是多行注释
# 床字符串中可以防止任何内容，包括双引号，单引号等，如果床字符串没有赋值给任何变量
# 这个字符串就会被解释器忽略，当做多行注释处理
s = '''这是一个长字符串，可以使用'单引号'，
和"双引号",\n转义字符可以吗'''
print(s)
# 也可以使用转义字符进行长字符串，字符串换行不会中断
s1 = '这是一个长字符串\
可以使用'
print(s1)
# 如果表达式需要换行，同样可以使用转义字符(\)进行换行
num = 20 + 3 / 4 + \
    2 * 3
print(num)

# 原始字符串
# 因为‘\’在字符串中有特殊的含义。如果需要原样输出‘\’则需要对其进行转义，即 \\
# 原始字符串是以r开头的，字符串中的内容不会被当做特殊字符处理
s1 = r'D:\''  # 原始字符串中，引号仍需转义，但是转义字符会原样输出
print(s1)
# s2 = r's'd'  无法解析

# bytes  字节串
# python3 新增内容
# 字符串  由多个字符组成，以字符为单位进行操作；
# bytes由多个字节组成，以字节为单位进行操作
# bytes 和 string （str）除了操作的数据单元不一样之外，支持的方法都是一样的，bytes也是不可变的序列
# bytes对象只负责以字节序列来记录数据，数据内容由程序决定。采用适当的字符集，字符串和bytes之间可以互转
# 如果 字符串 的内容都是ASCII字符，则可以通过在字符串之前添加 b 来构建bytes
# 调用bytes()函数将字符串按指定字符集转换成字节串，如果不指定字符集，默认使用UTF-8
# 调用字符串分身的encode()函数，将字符串按指定字符集转换成字节串，如果不指定，默认UTF-8
# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes值
b2 = b''
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
# 调用bytes方法将字符串转换成bytes对象
b4 = bytes('我爱这个', encoding='utf-8')
# 利用字符串的encode() 方法编码成bytes，默认ute-8
b5 = '我爱这个'.encode()
print(b4, b5, sep='\n')
# decode()解码
b6 = b5.decode('GBK')  # 乱码，因为不是对应的字符集
b6 = b5.decode('utf-8')     # 我爱这个
print(b6)
