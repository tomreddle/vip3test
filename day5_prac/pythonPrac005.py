# python实现冒泡排序
# 一组数，一次比较相邻的两个数，小的放前面，大的放后面,一次往后，第一次比完左后一个数就是最大的
# 6,3,8,2,9,1


def bubble_sort(argus):
    length = len(argus)     # 列表的长度
    for i in range(length-1):       # 总共需要比较几趟
        for j in range(length-1-i):     # 每趟需要比较多少次
            if argus[j] > argus[j+1]:
                argus[j], argus[j+1] = argus[j+1], argus[j]    # 先封包，后解包  x, y = y, x; 1.xy = y, x ; 2.x, y = xy
                # a = argus[j]
                # argus[j] = argus[j+1]
                # argus[j + 1] = a
    return argus


lis = [6, 3, 8, 2, 9, 1]
lis1 = bubble_sort(lis)
print(lis1)



