import random
#输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
    # 0<= <60  e
    # 60<= <70 d
    # 70<= <80 c
    # 80<= <90 b
    # 90<= <=100 a
a = int(input('>>>'))
if 70 <= a <= 100:
    if a >= 90:
        print('A')
    elif a >= 80:
        print('B')
    else:
        print('C')
elif 0 <= a < 70:
    if 0 <= a < 60:
        print('E')
    else:
        print('D')
else:
    print('error')


#定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
s = [0,1,3,4,9,12,33,56,98,112,235]
#b = random.randint(0,1000)
b = int(input("请输入一个整数："))
if s.count(b):
    print("{} 在列表中".format(b))
else:
    print("{} 不在列表中".format(b))

#求10阶乘
a = 1
for i in range(1,11):
    a = a * i
print(a)

#s = []
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


#求10000以内的质数
#质数只能被1和其自身整除
#x = int(input('>>>>'))
s = []
s1 = list(range(2,100000))
for n in s1:
    j = 0
    for i in range(2,n):
        if n % i == 0:
            j = j + 1
            break
    if j == 0:
        s.append(n)
print(s)
