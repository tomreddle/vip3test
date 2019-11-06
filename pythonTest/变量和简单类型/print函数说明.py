print(40, '\t', end='')
print(50, '\t', end='')
# 可是使用print()函数中的file参数将结果输出至指定文件中
# print(values, sep=' ', end='\n', file=sys.stdout, flush=False)
# flush 用来控制输出的缓存，一般保持为False
f = open(r'C:\Users\hyr\Desktop\aaaa.txt', 'w')
print('海上升明月，', file=f)
print('天涯共此时，', file=f)
f.close()
