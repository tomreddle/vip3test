# 列表和元组的区别：列表是可变的；原则是不可变的，元组一旦构建出来，程序就不能修改元组

# 通过索引使用元素
# 列表和原则都可以通过索引来访问元素，索引都是从0开始的，第一个元素的索引是0，以此类推
# 它们还支持使用负数索引，倒数第一个元素的索引是-1，一次类推
# 列表的元素相当于一个变量，程序可以对它重新赋值
# 元组的元素相当于一个常量，程序只能使用它的值，不能对它重新赋值

# 使用列表和元组的元素
a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
print(a_tuple)      # ('crazyit', 20, 5.6, 'fkit', -17)
# 访问第一个元素
print(a_tuple[0])   # crazyit
# 访问第二个元素
print(a_tuple[1])   # 20
# 访问最后一个元素
print(a_tuple[-1])      # -17
# 访问倒数第二个元素
print(a_tuple[-2])      # fkit

# 子序列
# 子序列类似于字符串的操作，使用索引获取中间的一段，这种用法呗成为切片(slice)
# 用法： [start: end: step]
# 其中，start、end两个索引值都可以使用正数和负数，其中负数表示从倒数开始；step是步长，使用负数没有意义
# 切片的语法表示，从start索引开始（包含）到end索引元素结束（不包含）的所有元素
# 示例使用切片获取元素
a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
# 访问第二个到第四个（不包含）的所有元素
print(a_tuple[1: 3])        # (20, 5.6)
# 访问倒数第三个到倒数第一个（不包含）的所有元素
print(a_tuple[-3: -1])      # (5.6, 'fkit')
# 访问第二个到倒数第二个（不包含）的所有元素
print(a_tuple[1: -2])       # (20, 5.6)
# 访问倒数第三个到第五个（不包含）的所有元素
print(a_tuple[-3: 5])       # (5.6, 'fkit', -17)

# 使用步长参数间隔获取元素
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 访问第三个到第九个（不包含），间隔2的所有元素
print(b_tuple[2: 8: 2])     # (3, 5, 7)
# 访问第三个到第九个（不包含），间隔为3的所有元素
print(b_tuple[2: 8: 3])     # (3, 6)
# 访问第三个到倒数第二个（不包含），间隔为2的所有元素
print(b_tuple[2: -2: 2])    # (3, 5, 7)

# 加法
# 列表和元组支持加法运算，加法的和就是连个列表或者两个元组所包含的所有元素的总和
# 列表只能对列表相加；元组只能对元组相加；元组不能和列表相加
# 示例加法
a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
# 计算元组相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple)        # ('crazyit', 20, -1.2, 127, 'crazyit', 'fkit', 3.33)
print(a_tuple)      # ('crazyit', 20, -1.2) 不改变原来元组的内容
print(b_tuple)      # (127, 'crazyit', 'fkit', 3.33)    不改变原来元组的内容
print(a_tuple + (-20, -30))     # ('crazyit', 20, -1.2, -20, -30)

# 列表和元组相加会报错
# print(b_tuple + [20, 30])
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c']
# 计算列表相加
sum_list = a_list + b_list
print(sum_list)     # [20, 30, 50, 100, 'a', 'b', 'c']
print(a_list + ['fkit'])    # [20, 30, 50, 100, 'fkit']

# 列表和元组可与进行乘法运算
# 就是讲他们所包含的元素重复N次
# 乘法示例
a_tuple = ('crazyit', 20)
print(a_tuple * 3)      # ('crazyit', 20, 'crazyit', 20, 'crazyit', 20)
a_list = [30, 'Python', 2]
mul_list = a_list * 3
print(mul_list)         # [30, 'Python', 2, 30, 'Python', 2, 30, 'Python', 2]

# 对列表和原则同事进行加法和乘法
order_endings = ('st', 'en', 'rd')\
                + ('th',) * 17 + ('st', 'en', 'rd')\
                + ('th',) * 7 + ('st',)
print(order_endings)
day = input("请输入日期(1-31)：")
day_int = int(day)
print(day + order_endings[day_int - 1])
# 上面程序中需要注意的是('st',)，是因为字符串加上括号并不是元组，这个时候('st') 和 'st'是一样的，都是字符串
# 为了表示一个元素的元组，则必须在唯一的元素后面加上英文逗号
a = ('a',)
print(a)

# in运算符
# 用于判断列表或者元组中是否包含某个元素
a_tuple = ('crazyit', 20, -1.2)
print(20 in a_tuple)            # True
print(1.2 in a_tuple)           # False
print('fkit' not in a_tuple)    # True

# 长度len()、最大值max()、最小值min()
# 元素都是数值的元组
a_tuple = (20, 10, -2, 15.2, 102, 50)
# 计算最大值
print(max(a_tuple))
# 计算最小值
print(min(a_tuple))
# 计算长度
print(len(a_tuple))
# 都是字符串的列表
b_list = ['crazyit', 'fkit', 'Python', 'Kotlin', 'fkita']
# 计算最大值（一次比较每个字符的ASCII码值，先比较第一个字符，若相同在比较第二个字符，以此类推）
print(max(b_list))      # fkita    26个小写字母的ASCII码为97-122
# 计算最小值
print(min(b_list))      # Kotlin  26个大写字母ASCII码为65-90
# 计算长度
print(len(b_list))      # 5

# 序列封包和序列解包
# Python提供了序列封包（Sequence Packing）和序列解包（Sequence Unpacking），python支持两种赋值方式
# 程序将多个值赋给一个变量时，Python会自动将多个值封装成元组——序列的封包
# 程序允许将序列（元组或列表）直接赋值给多个变量，此时序列的各元素会被一次赋值给每个变量
# （要求序列的元素个数和变量个数相同）——序列解包
# 示例
# 序列封包
vals = 10, 20, 30
print(vals)     # (10, 20, 30)
print(type(vals))   # <class, 'tuple'>
print(vals[1])      # 20

# 序列解包
a_tuple = tuple(range(1,10,2))
a, b, c, d, e = a_tuple
print(a, b, c, d, e)

# 序列解包
a_list = ['fkit', 'crazyit']
a_str, b_str = a_list       # 1 3 5 7 9
print(a_str, b_str)     # fkit crazyit

# 在赋值中同事运用封包和解包，接可以让赋值运算符支持同事将多个值赋给多个变量
x, y, z = 10, 20, 30
print(x, y, z)      # 10 20 30
# 上面的程序相当于先封包，然后再解包
xyz = 10, 20, 30
x, y, z = xyz
print(x, y, z)      # 10 20 30

# 在序列解包时，允许只解出部分变量，剩下的依然使用列表变量保存
# 这种解包方式在变量的左边添加 * 号，就代表该变量代表一个列表
first, second, *third = range(10)
print(second)       # 1
print(third)  # [2, 3, 4, 5, 6, 7, 8, 9]
# last保存最后一个元素，begin保存前面剩下的元素
*begin, last = range(10)
print(begin)    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last)     # 9
# first保存第一个元素，last保存最后一个元素，middle保存剩余元素
first, *middle, last = range(10)
print(first)    # 0
print(middle)   # [1, 2, 3, 4, 5, 6, 7, 8]
print(last)     # 9

