# 给定奇数n ，输出（横、坚、斜的总和相等）
num = 3
lis = [[0] * 3]  # 定义一个长度为3的列表
# 定义一个3*3的列表
for i in range(3):
    lis += [[0] * 3]
print(lis)
lis[0][1] = 1
x = 0   # 坐标初始化
y = 1   # 坐标初始化（0,1）
for j in range(1, 9):
    j = j + 1
    x = x - 1
    y = y + 1
    # 判断坐标位置情况，并据此赋值
    if y > (num - 1) and x < 0:
        x = x + 2
        y = y - 1
        lis[x][y] = j
    elif x < 0:
        x = num - 1
        lis[x][y] = j
    elif y > num - 1:
        y = 0
        lis[x][y] = j
    else:
        if lis[x][y] == 0:
            lis[x][y] = j
        elif lis[x][y] != 0:
            x = x + 2
            y = y - 1
            lis[x][y] = j
for a in range(num):
    for b in range(num):
        # rjust表示输出01，02，03等这种格式，可看我上篇博文介绍
        print(str(lis[a][b]).rjust(2, '0'), end=' ')
    print(' ')
