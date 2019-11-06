# 实现从excel中读取数据并返回对应的接口数据列表
import xlrd, os
# 读取excel先定位excel的位置和名称   路径 和名称
# 获取excel中所有sheet的名称列表  然后去判断sheet的数量(可用于循环)
# 循环实现读取每一个sheet中的内容
# 将excel中每一个sheet中对应序号的内容拼接，装入list中返回


class Readexcel(object):
    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    # 重新封装打开excel方法，并返回引用对象
    def open_excel(self):
        return xlrd.open_workbook(self.path + '\\' + self.file_name)

    # 读取urlSheet的内容，并装入url列表中
    def readurlsheet(self):
        url = []
        sheet = self.open_excel().sheet_by_name('urlSheet')
        for i in range(1, sheet.nrows):
            row_value = sheet.row_values(i)
            url.append(row_value)
        return url

    # 读取paramSheet的内容，装入parm列表
    def readparasheet(self):
        parm = []
        sheet = self.open_excel().sheet_by_name('paramSheet')
        for i in range(1, sheet.nrows):
            row_value = sheet.row_values(i)
            parm.append(row_value)
        return parm

    # 读取assertSheet的内容，装入assert1列表中
    def readassertsheet(self):
        assert1 = []
        sheet = self.open_excel().sheet_by_name('assertSheet')
        for i in range(1, sheet.nrows):
            row_value = sheet.row_values(i)
            assert1.append(row_value)
        return assert1

    # 按ID拼接三个列表
    # 列表interfacemessage中内容分别是id，hostip/域名，请求方法，接口参数，预期结果
    def tatol(self):
        url = self.readurlsheet()
        para = self.readparasheet()
        assert_result = self.readassertsheet()
        interfacemessage = []
        if len(url) == len(para) and len(para) == len(assert_result):
            for i in range(len(url)):
                del para[i][0]
                del assert_result[i][0]
                interfacemessage.append(url[i] + para[i] + assert_result[i])
            return interfacemessage
        else:
            return None


if __name__ == '__main__':
    a = Readexcel(r'C:\Users\hyr\Desktop\learning\第三天', 'data.xls')
    print(a.readurlsheet())
    print(a.readparasheet())
    print(a.readassertsheet())
    print(a.tatol())




