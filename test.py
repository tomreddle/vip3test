

'''
多行
注释注意缩进
不缩进会有问题（暂不知道）
'''
a=5
b=2.5
c='Hello'
#python中双引号和单引号效果相同，但

print(type(a))
print(type(b))
print(type(c))
print('let\' go')

#input()函数，从键盘输入字符串
#d = input('please input something:')
#print(d,type(d))#python 2.x支持多类型输入

#多数据同时录入
#x,y =input('>>>').split(',')
#split() 默认空格隔开，其他符号间隔需自定义
#print(x,y)

#另外一种输出方式
print("%d,%f,%s"%(a,b,c))

#format()回去自己看
print('{}'.format(a))
print('{0},{1}'.format(a,b))

'''
元组/列表/序列
'''

s1 = (1,2,3)#tuple 值不可变
s = [1,2,3,4,5,6,7,8,9]#list 值可以改变
#输出倒数第三个元素
print(s[-3])
#输出468
print(s[3],s[5],s[7])
print(s[3::2])

#定义1-999的元组
print(list(range(1,1000)))

#range()函数
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))

#元组的操作
#逆序
s.reverse()
print(s)
#reverse()函数没有返回值，直接打印为none
print(s.reverse())


#ctrl+/快捷方式注释


s.insert(-6,123)
print(s)

#extend()拼接
#返回最大值max(s)
print(s)
print(max(s))
#返回最小值min(s)
print(min(s))
#返回元组的列表
print(len(s))
#删除del s[n] 删除下标为n的元素
del s[3]
print(s)
#获得元素的下标s.index(n) n为元素  重复元素怎么办？第一个?是第一个
print(s.index(2))
s.append(2)
print(s)
print(s.index(2))
#清空列表
s.clear()
print(s)
#检查元素是否在列表中
x = 3 in s
y = 4 not in s
print(x)
print(y)

s3 = [11,13,5,7,0,56,23,34,72]
#最大值，最小值，共多少个元素
print(max(s3))
print(min(s3))
print(len(s3))
#获取56元素的位置
print(s3.index(56))
#追加元素7
s3.append(7)
print(s3)
#删除元素0
del s3[4]
print(s3)
#排序列表（大到小）
 # s3.sort()
 # s3.reverse()
 # print(s3)

#将列表[66,67,68]原列表组合
s4 = [66,67,68]
s3.extend(s4)
print(s3)

#集合
'''
无序，不重复，无法使用下标引用
'''
ss = {1,3,2}
ss.add(4)
print(ss)
ss.add(4)#加了白加
print(ss)
ss.remove(3)
print(ss)
#ss.remove(3)
print(ss)

ss.discard(4)
print(ss)
ss.discard(4)
print(ss)
ss.clear()
print(ss)


sss = {'a':10,'b':20,'c':15}
print(sss.keys())
print(sss.values())
print(type(sss.keys()))
print(sss.items())
del sss['a']
print(sss)
sss.clear()
print(sss)

h = input('>>>')
print(int(h))