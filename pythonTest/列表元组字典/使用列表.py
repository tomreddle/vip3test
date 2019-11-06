# 创建列表
# 除了使用方括号语法创建列表之外，Python还提供了内置函数list()来创建列表
# list()函数可将元组、区间（range）等对象转换为列表
a_tuple = ('crazyit', 20, -1.2)
# 将元组转换为列表
a_list = list(a_tuple)
print(a_list)       # ['crazyit', 20, -1.2]
a_range = range(1, 5)
print(a_range)      # range(1, 5)
# 将区间转换为列表
b_list = list(a_range)
print(b_list)       # [1, 2, 3, 4]
# 创建区间时还指定了步长
c_list = list(range(4, 20, 3))
print(c_list)       # [4, 7, 10, 13, 16, 19]


# 与list()函数对应的还有tuple()函数，用于将元组、区间（range）等对象转换为元组
# 将列表转换为元组
a_list = ['crazyit', 20, -1.2]
a_tuple = tuple(a_list)
print(a_tuple)       # ('crazyit', 20, -1.2)
a_range = range(1, 5)
print(a_range)      # range(1, 5)
# 将区间转换为元组
b_tuple = tuple(a_range)
print(b_tuple)       # (1, 2, 3, 4)
# 创建区间时还指定了步长
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)       # (4, 7, 10, 13, 16, 19)

# 增加列表元素 append()
# 使用append()函数将传入的参数追加到列表的最后面
# 可以接受单个值，也可以接受元组、列表等，但该方法只是将元组、列表等当做单个元素，嵌套在列表中
a_list = ['crazyit', 20, -1.2]
# 追加元素
a_list.append('fkit')
print(a_list)       # ['crazyit', 20, -1.2, 'fkit']
a_tuple = (3.4, 5.6)
# 追加元组
a_list.append(a_tuple)
print(a_list)       # ['crazyit', 20, -1.2, 'fkit', (3.4, 5.6)]
# 追加列表
a_list.append(['a', 'b'])
print(a_list)       # ['crazyit', 20, -1.2, 'fkit', (3.4, 5.6), ['a', 'b']]

# append()可以将列表嵌套至列表中
# 使用extend()可以将列表中的元素追加到前一个列表中，成为一个整体
b_list = ['a', 30]
# 追加元组中的所有元素
b_list.extend((-2, 3.1))
print(b_list)       # ['a', 30, -2, 3.1]
# 追加列表中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list)       # ['a', 30, -2, 3.1, 'C', 'R', 'A']
# 追加区间中的元素
b_list.extend(range(97, 100))
print(b_list)       # ['a', 30, -2, 3.1, 'C', 'R', 'A', 97, 98, 99]

# 如果想在列表中间添加元素，可以使用insert()方法，使用insert()方法要指定将元素插入列表的哪个位置
c_list = list(range(1, 6))
print(c_list)       # [1, 2, 3, 4, 5]
# 在索引3处插入字符
c_list.insert(3, 'CRAZY')
print(c_list)       # [1, 2, 3, 'CRAZY', 4, 5]
# 在索引3处插入元组，元组被当做一个元素
c_list.insert(3, tuple('crazy'))
print(c_list)   # [1, 2, 3, ('c', 'r', 'a', 'z', 'y'), 'CRAZY', 4, 5]

# 删除列表元素
# 使用del 语句删除列表的元素，还可以用于删除变量
# remove()删除指定内容，如果没有就会报错
# clear()清空整个列表的所有元素
# pop()删除指定元素并返回被删除的元素
