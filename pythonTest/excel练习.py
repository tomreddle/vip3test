import xlrd
import xlrd, xlwt
import xlutils.copy

# 打开excel
read_excel = xlrd.open_workbook(r'.\data\excel1.xlsx')
# 获取读入的文件的sheet
sheet_excel = read_excel.sheet_by_name('Sheet1')
sheet_name = read_excel.sheet_names()
sheet_name1 = read_excel.sheet_by_index(0)
print(sheet_name)
print(type(sheet_name))

# 获取sheet的最大行数和最大列数
n_rows = sheet_excel.nrows
n_cols = sheet_excel.ncols
print(n_rows, n_cols)

# 获取单元格的值
params_excel = sheet_excel.cell(1, 1)
print(type(params_excel))
print(params_excel)

# 获取某行、某列的值
row_value = sheet_excel.row_values(0)
print(row_value)
col_value = sheet_excel.col_values(1)
print(col_value)

rb = xlrd.open_workbook(r'./data/excel1.xlsx')
wb = xlutils.copy.copy(rb)
ws = wb.get_sheet(0)
ws.write('1233', 'append')