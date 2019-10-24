# 导入
import xlrd,xlwt

# 读取excel
# 打开excel  open
readexcel = xlrd.open_workbook(r'E:\code\vip3test\day3_prac\test.xlsx')

# 读取文件中的sheet
# sheet = readexcel.sheet_by_index(0)  # 从0开始
sheet = readexcel.sheet_by_name('Sheet1')      # 按sheet的名称读取
# allsheetnames = readexcel.sheet_names()        # 获取所有sheet的名称列表
# print(allsheetnames)

a = sheet.nrows
b = sheet.ncols
print(a, b, sep='\t')

# 获取每一行的内容并存入列表中
list1 = []
for i in range(1, sheet.nrows):
    row_value = sheet.row_values(i)
    list1.append(row_value)
print(list1)
