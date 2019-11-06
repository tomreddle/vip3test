# 从标准输入读取两个整数并打印两行，其中第一行输出两个整数的整除结果；第二行输出
# 两个整数的带小数的除法结果。不需要执行任何四舍五入或格式化操作。
a = int(input("a>>>>>>:"))
b = int(input("b>>>>>>:"))
print(a // b)
print(a / b)

# 用户输入一个字符串和 一个子串，程序必须打印出给定子串在目标字符串中出现的次数 。
# 字符串遍历将从左到右进行，而不是从右到左 。 例如给定'ABCDCDC’和’CDC'，程序输出“ 2 ”。
str1 = input('>>>>>>>>')
str1_part = input('>>>>>>>>')
count = 0
for i in range(len(str1)):
    if str1[i:i+len(str1_part)] == str1_part:
        count += 1
print(count)

# 本程序要实现一个功能：用户输入一个字符串，修改该
# 字符串中哪个位置的字符，程序就会输出修改后的结果。比如用户输入'fkjava.org'  6  -
# 输出‘fkjava-org’
str2 = input('>>>>>>')
str3 = int(input('>>>>>>>'))
str4 = input('>>>>>>>')
print(str2.replace(str2[str3], str4))