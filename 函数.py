#简单计算器
'''def add(x,y):
    return x+y

def plus(x,y):
    return x-y

def acc(x,y):
    return x*y

def div(x,y):
    return x/y

a = 1
b = 2
while 1:
    x = input("请输入您想进行的运算+-*/：")
    if x == '+':
        print(add(a,b))
    elif x == '-':
        print(plus(a,b))
    elif x == '*':
        print(acc(a,b))
    elif x == '/':
        print(div(a,b))
    else:
        print("输入有误！")
    y = input("继续请按任意键，如要退出请按n：")
    if y == 'n':
        break
'''

#默认参数函数
#需注意，默认参数一定要后，选定参数在前；参数值变化小的设置为默认参数
def sum(a,b=1):
    return a+b

print(sum(1))
print(sum(1,3))
#关于参数指向不可变对象不太懂

#可变参数函数：函数的参数个数可变,允许传入0-n个人以参数，也可使用已有列表传参
def calc(*numbers):
    print(*numbers)
    print(numbers)
    sum = 0
    for n in numbers:
        sum += n
    return sum

num = [1,2,3]
print(calc(*num))

#关键字参数
def person(name,age,**kwargs):
    print('name',name,'age',age,kwargs)

person('小明',16,sex = 'male')
person('小明1',17)

#也可使用字典传参
extra = {'city':'beijing','job':'Engineer'}
person('小明1',17,**extra)