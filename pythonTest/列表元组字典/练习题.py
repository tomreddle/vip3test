# 提示用 户输入 N 个字符串 ，将它们封装成元组，然后计算并输入该元组乘以 3 的结果，
# 再计算并输出该元组加上（’tkjava’，’crazyit＇）的结果 。
str_list = []
for i in range(1, 4):
    str1 = input('请输入第{}个字符串:'.format(i))
    str_list.append(str1)

str_tuple = tuple(str_list)
print(str_tuple)
str_tuple1 = str_tuple * 3
print(str_tuple1)
str_tuple2 = str_tuple1 + ('tkjava', 'crazyit')
print(str_tuple2)


# 给定 一个 list ，将该列表的从 start 到 end 的所有元素复制到另 一个 list 中
test_list = [1, 3, 5, 2, 77]
test_list1 = test_list[:]
print(test_list1)       # [1, 3, 5, 2, 77]

test_list2 = []
for i in test_list:
    test_list2.append(i)
print(test_list2)       # [1, 3, 5, 2, 77]

# 用户输入一个整数 n ，生成长度为 n 的列表，将 n 个随机数放入列表中

