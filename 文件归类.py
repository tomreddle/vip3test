import os
import shutil

# 设置文件路径
path = 'E:\\code\\work\\'
# 获取文件列表
file_name = os.listdir(path)
print(file_name)
for file_name in file_name:
    # 根据文件列表得到文件后缀
    # print(file_name)
    file_message = os.path.splitext(path + file_name)
    file_message[-1]
    print(file_message[-1].strip('.'))
# 根据文件后缀判断当前路径下是否有对应文件夹
# 有则将文件放入改文件夹
# 没有则新建文件夹 并将对应文件放入对应文件夹
    if os.path.exists(path + file_message[-1].strip('.')):
        shutil.move(path + file_name, path + file_message[-1].strip('.') + '\\' + file_name)
    else:
        os.makedirs(path + file_message[-1].strip('.'))
        shutil.move(path + file_name, path + file_message[-1].strip('.') + '\\' + file_name)
