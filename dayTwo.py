
'''
#计算1+2+3+4……+100的和
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1

print('1+2+3+4……+100 = {}'.format(sum))

#求100以内能被3整除的数，并将作为列表输出
s =[]
for i in range(1,101):
    if i % 3 == 0:
        s.append(i)

print(s)

#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
s1 = [1,2,3,4,3,4,2,5,5,8,9,7]
s2 = []
'''
'''
#根据用户输入的计算符号计算结果
def calc(x,y,s):
    if s == '+':
        return x + y
    if s == '-':
        return x - y
    if s == '*':
        return x * y
    if s == '/':
        return x / y
symbol = input('请输入想进行的运算：（+、-、*、/）')
a = int(input('a>>>>>'))
b = int(input('b>>>>>'))
c = calc(a,b,symbol)
print('{} {} {} ={}'.format(a,symbol,b,c))

d,e = input('>>>>>>>').split(' ')
print(d,e)
'''
'''
def add_end(L = []):
    L.append('end')
    return L

print(add_end())
print(add_end())
'''
'''
#可变参数传参
def calc(*numbers):
    print(numbers)
    print(*numbers)
    sum = 0
    for i in numbers:
        #sum += i
        print(i)
    #return sum

L = [1,2,3,4]
c = calc(L)
print(c)
print('~~~~~~~~~')
d = calc(3,3,3,3)
print(d)
print('~~~~~~~~~')
e = calc()
print(e)


#关键字参数传参 **arguments
def person(**argus):
    print(argus)
    print(argus.keys())
    print(argus.values())

D = {'a':55,'b':66}
person()
print('~~~~~~~~~')
person(c = 77)
print('~~~~~~~~~')
person(**D)


def div(a,b):
    try:
        print(a/b)
    except BaseException as msg1:
        print(msg1)

div(2,0)


def calc(x,y,s):
    try:
        if s == '+':
            print(x + y)
        elif s == '-':
            print(x - y)
        elif s == '*':
            print(x * y)
        elif s == '/':
            print(x / y)
            # except ZeroDivisionError as msg:
            #     print(msg)
            # except Exception as msg:
            #     print(msg)
        else:
            print('*************')
    except ZeroDivisionError as msg:
            print(msg)
    else:
        print('111111111')
    finally:
        print('222222')

symbol = '7'#input('请输入想进行的运算：（+、-、*、/）')
a = 1 #int(input('a>>>>>'))
b = 1 #int(input('b>>>>>'))
calc(a,b,symbol)
#print('{} {} {} ={}'.format(a,symbol,b,c))
'''

#文件读取写入
f = open(r'C:\Users\hyr\Desktop\第二天\data.txt','r+')
s = f.readlines()
print(s)
#f.seek(0)
#print(f.read(3))
s1 = []
#strip()函数 去除首尾指定的字符
for i in s:
    s1.append(i.strip('\n'))
    #s1.append(i.replace('\n',''))
print(s1)
f.close()
s1.sort()
print(s1)
m = open(r'C:\Users\hyr\Desktop\第二天\backup.txt','w+')
m.writelines(s1)
m.seek(0)
print(m.readlines())
f.close()

#replace(a,b) 用b 替换 a 返回一个副本
with open(r'C:\Users\hyr\Desktop\第二天\data.txt','r+') as a:
    s = a.readlines()
    print(s)


#string.join(list)