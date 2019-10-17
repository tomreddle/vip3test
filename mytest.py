# import mymodule

# mydodule.fun1()
# mydodule.fun2()

# f = open(r'E:\code\data.txt', 'r')
# 读取文件内所有内容
# print(f.read())
# 定位到文件开始
# f.seek(0)
# 读取文件内两个字节的内容
# print(f.read(2))
# 定位到文件第二行
# f.seek(1)
# 读取文件的所有内容，并生成行的列表
# print(f.readlines())
# 定位到文件第二行
# f.seek(0)
# 读取文件的某一行
# print(f.readline())
# f.close()
#
# with open(r'E:\code\data.txt', 'a') as h:
#     m = ['hello world!']
#     h.write(m)
#
# f = open(r'E:\code\data.txt', 'r')
# print(f.read())
# f.close()

# 私有方法和私有属性
# 私有方法和私有属性只能有在类的内容进行调用


# class A:
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#
#     def test1(self):
#         print("公有方法")
#
#     def __test2(self):
#         print("私有方法")
#
#     def test3(self):
#         print("公有方法调用私有方法")
#         self.__test2()
#         print(self.num1)
#         print(self.__num2)
#
#
# class B(A):
#     def test4(self):
#         # self.__num2
#         # self.__test2()
#         self.test1()
#
#
# b = B()
# b.test4()
#
# a = A()
# a.test3()


# 字符串操作
str2 = "1hello world!"
# capitalize() 将字符串的首字母转大写，不改变原字符串，如果不能转就不变
str1 = str2.capitalize()
print(str1)
# count() 统计字符串中某字符出现的次数，隐藏参数 开始位置  结束位置
print(str2.count('l', 4, 11))
# find() 检测字符串是否包含否字符，如果包含则返回字符的索引值，否则返回-1(如果出现多次则返回第一次出现的索引值)
print(str2.find('a'))
# isalpha() 检测不为空的字符串是否全部为字母，是 返回True 否 返回False
print(str2.isalpha())
# isdigit() 检测不为空的字符串是否全部为数字，是 返回True 否 返回False
print(str2.isdigit())
# str.join(seq) 将序列以str作为分隔符重新合并为一个字符串
s = ['a', 'b', 'c', 'd']
s1 = '\t'.join(s)
print(s1)
# str.replace(str1, str2, num) 讲str中的str1替换成str2，num指定替换次数，默认为count(str1)
print(str2.replace('l', '\n', 1))
# str.strip(str1) 讲str首尾的str1删除（执行lstrip(str1) 和rstrip(str1)）
print(str2.strip('!'))
print(str2.lstrip('1'))
print(str2.rstrip('!'))


# 读取文件内容
with open(r'E:\code\test.txt', 'r') as test:
    # 定义列表存放L开头的姓名
    l = []
    # 定义列表存放出生日期
    age = []
    # 定义列表存放女性信息
    female = []
    s = test.readlines()
    print(s)
    for i in s:
        print(i)
        if i.find('L') != -1:
            l.append(i.split('|')[0])
        age.append(i.split('|')[-1].strip())
        if i.find('女') != -1:
            female.append(i.strip())
    # for line in test:
    #     # line.strip()
    #     str3 = line.strip().split('|')
    #     if line.find('l') != -1:
    #         l.append(str3[0])
    #     age.append(age.append(str3[-1]))
    print(l)
    print(sorted(age))
    print(female)
    # print(L)
