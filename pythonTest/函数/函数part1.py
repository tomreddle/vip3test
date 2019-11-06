# 定义函数前应该清楚：
# 1.函数需要几个参数，即需要几个动态变化的数据
# 2.函数需要传出几个数据，这些被定义为返回值
# 3.函数的内部实现

# 函数在使用之前必须先定义函数
# 语法：
# def 函数名(形参列表):
#     //由领条到多条可执行语句组成的函数
#     [return [返回值]]
# 函数名：从语法角度来看，函数名只要是合法的标识符即可；
# 从程序的可读性角度来看，函数名应该由一个或多个有意义的单词连缀而成，每个单词字母全部小写，单词与单词之间使用下划线连接
# 形参列表：用于定义该函数可以接受的参数。形参列表由多个参数名组成，多个形参名之间以英文“,”隔开。
# 定义函数时一旦指定了参数列表，调用该函数时就必须穿入对应的参数值，谁调用函数，谁负责为形参赋值。

# 在函数体中多条执行语句之间有严格的执行顺序，排在函数体前面的语句总是先执行，排在函数体后面的语句总是后执行。
# 示例


# 定义一个函数，声明两个形参
def my_max(x, y):
    # 定义一个变量z，该变量等于x，y总较大的值
    z = x if x > y else y
    # 返回变量z的值
    return z


# 定义一个函数，声明一个形参
def say_hi(name):
    print("=====正在执行say_hi()函数=====")
    return name + ",您好！"


a = 6
b = 9
# 调用my_max()函数，将返回值赋给result变量
result = my_max(a, b)
print("result:", result)
# 调用say_hi()函数，直接打印函数的返回值
print(say_hi("孙悟空"))


# 多个返回值
# 如果程序需要多个返回值，可以将多个值包装秤列表之后返回，也可以直接返回多个值
# 如果python函数直接返回多个值，python会自动将多个返回值封装成元组


def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum/count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
tp = sum_and_avg(my_list)
print(tp)
s, avg = sum_and_avg(my_list)
print(s, avg)


# 递归函数：在函数体内调用它自身


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return 2 * fn(n - 1) + fn(n - 2)


# 输出fn(10)的值
print("fn(10)的结果是：", fn(100))
# 递归可以用于遍历路径下的所有文件，需要注意的是，递归一定要向已知的方向进行

