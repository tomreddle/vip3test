# 简单递归实现 递归实现斐波那契数列
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print([fibonacci(x) for x in range(10)])
