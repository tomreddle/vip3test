# 字典是存放具有映射关系的数据结构
# 字典相当于保存两组数据，一组是关键数据，成为key；另一组可以通过key来访问，成为value
# 由于字典中的key是非常关键的数据，而且程序还需要通过key来访问value，所以字典中的key不允许重复
# 字典的创建有两种方式
# 方式一：通过花括号语法来创建
# 方式二：通过dict()函数来创建
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)       # {'语文': 89, '数学': 92, '英语': 93}
empty_dict = {}
print(empty_dict)   # {}
# 使用元组作为字典的key
dict2 = {(20, 30): 'good', 30: 'bad'}
# 元组可以作为key，但是列表不能作为key。这是因为字典要求key必须是不可变类型的

# 在使用dict()函数创建字典的时候，可以传入多个列表或者元组参数作为key-value对，每个列表或元组将被当成一个key-value对
# 因此这些列表或元组都只能包含两个元素
vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
# 创建一个字典
dict3 = dict(vegetables)
print(dict3)        # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
# 如果不为dict()传入任何参数，则会创建一个空的字典
dict5 = dict()
print(dict5)
# 还可以通过为dict指定关键字参数创建字典，此时字典的key不允许使用表达式
dict6 = dict(spinasch=1.39, cabbage=2.59)
print(dict6)    # {'spinasch': 1.39, 'cabbage': 2.59}

# 字典的基本用法
# 字典的操作都是基于key的，通过key访问value、添加key-value对、删除key-value对、
# 修改key-value对、判断指定的key-value对是否存在
# 通过key访问value使用的也是方括号语法，和元组和序列一样，只是这里方括号里放的是key
scores = {'语文': 89}
print(scores['语文'])     # 89
# 添加key-value对，只需为不存在的key赋值即可
scores['数学'] = 93
scores[92] = 5.7
print(scores)       # {'语文': 89, '数学': 93, 92: 5.7}

# 删除字典中的key-value对使用del语句
del scores['语文']
print(scores)       # {'数学': 93, 92: 5.7}

# 对现在存在的key-value对赋值，新的value会覆盖在原有的value，即修改原有的key-value对
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars)     # {'BMW': 8.5, 'BENS': 4.3, 'AUDI': 3.8}

# 判断字典是否包含指定的key可以使用in或 not in运算符，对于dict而言，in或not in都是局域key判断的
# 判断cars是否包含AUDI的key
print('AUDI' in cars)       # True
print('PORSCHE' in cars)        # False
print('LAMBORGHINI' not in cars)        # True

# 字典的常用方法
print(dir(dict))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# clear()  清空字典，使成为一个空字典
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)     # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars.clear()
print(cars)     # {}

# get()  根据key获取value，相当于加强版方括号语法
# 方括号语法中如果key不存在会引发KeyError；使用get()方法则不会，只会返回None
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.get('BMW'))      # 8.5
print(cars.get('PORSCHE'))  # None
# print(cars['PORSCHE'])      # KeyError

# update() 跟新指定key的value值，如果没有指定key值则插入改key-value对
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars.update({'BMW': 4.5, 'PORSCHE': 9.3})
print(cars)     # {'BMW': 4.5, 'BENS': 8.3, 'AUDI': 7.9, 'PORSCHE': 9.3}

# items()获取字典所有的key-value对
# keys()获取字典所有的key值
# values()获取字典所有的value值
# 三个方法返回的是dict_items\dict_keys\dict_values
# 可以使用list()函数将上述三个返回值转换为列表形式
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
ims = cars.items()      # dict_items([('BMW', 8.5), ('BENS', 8.3), ('AUDI', 7.9)])
print(type(ims))        # <class 'dict_items'>
print(list(ims))        # [('BMW', 8.5), ('BENS', 8.3), ('AUDI', 7.9)]
print(list(ims)[1])     # ('BENS', 8.3)
# 获取字典的key值
kys = cars.keys()
print(type(kys))        # <class 'dict_keys'>
print(list(kys))        # ['BMW', 'BENS', 'AUDI']
print(list(kys)[1])     # BENS
# 获取value值
vals = cars.values()
print(type(vals))       # <class 'dict_values'>
print(list(vals))       # [8.5, 8.3, 7.9]
print(list(vals)[1])    # 8.3

# pop()函数用于获取指定key对应的value，并删除该key-value对
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.pop('BMW'))      # 8.5
print(cars)     # {'BENS': 8.3, 'AUDI': 7.9}
# popitem()用于随机弹出字典中的一个key-value对
# 其实就是去除字典的最后一个key-value对，只不过字典中内容的顺序是不可知的，所以给人的感觉是随机的
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.popitem())       # ('AUDI', 7.9)
print(cars)                 # {'BMW': 8.5, 'BENS': 8.3}
# popitem()取出的是一个元组，可以通过解包的方式将key和value分别赋给两个变量
k, v = cars.popitem()
print(k, v, sep='\t')       # BENS	8.3

# setdefault()也是根据key值获取对应的value值
# 不同在于，如果key在字典中不存在时会先给这个不存在的key设置一个默认的value，然后再返回对应的value
# 即，如果key存在则返回指定的value；如果不存在则返回默认的value值
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.setdefault('PORSCHE', 9.2))
print(cars)     # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9, 'PORSCHE': 9.2}
print(cars.setdefault('BMW', 8))    # 8.5
print(cars)     # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9, 'PORSCHE': 9.2}

# fromkeys()方法使用给定的多个key值创建字典，这些key对应的value都是默认的None，也可以额外传入一个参数作为默认的value
# 该方法一般不会使用字典调用，通常使用dict类直接调用
a_dict = dict.fromkeys('a')
print(a_dict)       # {'a': None}
# 使用列表创建包含两个key的字典
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)       # {'a': None, 'b': None}
# 使用元组创建包含两个key的字典
b_dict = dict.fromkeys((13, 17))
print(b_dict)          # {13: None, 17: None}
# 使用元组创建包含两个key的字典，默认value
c_dict = dict.fromkeys((13, 17), 'good')
print(c_dict)       # {13: 'good', 17: 'good'}
d_dict = dict.fromkeys((13, 17, 13), 'good')
print(d_dict)
# 使用字典格式化字符串
temp = '书名是：%(name)s，价格是：%(price)010.2f，出版社是：%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子出版社'}
print(temp % book)      # 书名是：疯狂Python讲义，价格是：0000088.90，出版社是：电子出版社
book = {'name': '疯狂Kotiln讲义', 'price': 78.8, 'publish': '电子出版社'}
print(temp % book)      # 书名是：疯狂Kotiln讲义，价格是：0000078.80，出版社是：电子出版社
print(cars)
a = cars.copy()
print(a)
