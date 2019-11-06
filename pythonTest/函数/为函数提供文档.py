# 在函数的声明之后、函数体之前，这部分放函数的说明文档，
# 程序可以通过help()函数查看函数的书名文档，也可以通过函数的__doc__属性访问函数的说明文档


# 示例
def my_max(x, y):
    '''
    获取两个数值之间的较大值

    my_max(x, y)
        返回x,y变量中的较大值
    '''
    # 定义一个变量z，该变量等于x，y总较大的值
    z = x if x > y else y
    # 返回变量z的值
    return z


# 使用help()函数查看my_max()函数的帮助文档
help(my_max)
print(my_max.__doc__)
