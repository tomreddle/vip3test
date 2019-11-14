# 1、2、3、4能组成多少个不同且不重复的三位数，各是多少
# 每个数字开头的所有三位数，包括自身
lis = [1, 2, 3, 4]
result = [111, 222, 333, 444]
for i in lis:
    for j in lis:
        for k in lis:
                if i != j and j != k:
                    result.append(i*100 + j*10 + k)
print(result)

