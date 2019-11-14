import pymysql

# 此为实验python使用PyMySQL操作mysql数据库，平时使用时可将数据库配置放在config.ini中
# 数据库的连接及执行增删改查可封装起来以待使用
# 设置数据库配置
host = '127.0.0.1'
user = 'root'
passwd = 'root'
database = 'test'

# 简单pymysql操作数据库示例
# 数据库增删改查
db = pymysql.connect(host, user, passwd, database)  # 打开数据库连接
cursor = db.cursor()    # 建立游标对象
sql_select = '''select * from employee'''      # 待执行sql
a = cursor.execute(sql_select)     # 赋值给a可接收受执行sql影响的行数
print("受影响结果条数:{}".format(a))        # 2
data = cursor.fetchall()        # 获取结果  fetchall 获取全部  fetchone 获取一条
print(data)

# 增 excutemany()可一次执行多个sql,传参时要注意传参的方式；也可使用循环来实现
sql_insert = '''insert into employee values('{}', '{}', {}, '{}')'''
employee_id = '20191114'
employee_name = 'TomReddle'
employee_age = 35
employee_sex = 'M'
try:
    # 假想：是否可以使用此方法实现sql中各字段的参数化
    cursor.execute(sql_insert.format(employee_id, employee_name, employee_age, employee_sex))
    db.commit()     # 执行成功，提交数据
    print("数据插入成功")
except Exception as msg:
    db.rollback()   # 执行失败，数据库回滚
    print(msg)

# 根据用户的选择查询指定字段的值
user_select = input('请选择查询的字段：id，name,age,sex:')
select_params = '''select {} from employee'''.format(user_select)
cursor.execute(select_params)
data = cursor.fetchall()
# data1 = cursor.fetchmany(1)     # 如果在fetchall下面使用会返回空元组
print(data)
# for i in data1:
#     print(i)
print(cursor.rowcount)      # 获取受影响的行数

cursor.close()      # 关闭游标
db.close()          # 关闭数据库连接

# 改、删和增一样，主要异常的捕获，并注意在修改或更新数据库时db.commit()提交数据，
# 并在执行sql失败后及时回滚db.rollback()

# 可通过设定游标参数来指定获取数据的类型为字典（更直观？）
db1 = pymysql.connect(host, user, passwd, database)
cursor = db1.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select * from employee')
data = cursor.fetchall()
print(data)
cursor.close()
# [{'id': '20191108', 'name': 'BlackWidow', 'age': 35, 'sex': 'F'},
# {'id': '20191109', 'name': 'SteveRogers', 'age': 80, 'sex': 'M'},
# {'id': '20191114', 'name': 'TomReddle', 'age': 35, 'sex': 'M'}]
db1.close()
