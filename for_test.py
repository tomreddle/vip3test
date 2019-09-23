#while循环
'''
while 条件：
    循环体
    循环变量发生变化
'''

#使用while实现1+2+3+..+100求和
#定义循环变量
i = 1
#sum变量存放结果
sum = 0
#循环变量小于101则进入循环体，大于100则不进入
while i < 101:
    #计算i+(i-1)
    sum = sum + i
    #循环变量+1
    i = i + 1
#打印结果
print(sum)


#for循环
'''
for 变量 in 序列:
    循环体
'''
#求10阶乘
a = 1
for i in range(1,11):
    a = a * i
print(a)

#求100以内能被3整除的数，并将结果最为列表输出
s = []
for i in range(101):
    if i%3 == 0:
        s.append(i)
print(s)

#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
s1 = [1,2,3,4,3,4,2,5,5,8,9,7]
for i in s1:
    j = s1.index(i) + 1
    while j < len(s1):
        if i == s1[j]:
           del s1[j]
        j = j +1
#s1.sort()
print(s1)

#求斐波那契数列 1 2 3 5 8 13 ……
i = 1
s2 = [1,2]
a1 =  int(input("请录入您想循环的次数："))
while i :
    a = s2[i] + s2[i-1]
    s2.append(a)
    i = i +1
    if i == a1:
        break
print(s2)
