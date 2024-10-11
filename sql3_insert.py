import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',  # 主机名
    port=3306,  # 端口号
    user='root',  # 数据库用户名
    passwd='123456',  # 密码
    db='test1',  # 数据库名称
    charset='utf8'  # 编码格式
)
# 获取游标
cursor = connect.cursor()
# 插入数据
sql = "INSERT INTO student(Sno,Sname,Ssex,Sage,Sdept) VALUES (%s, %s, %s, %s, %s)"
data = [
    ('10001', 'Jack', '男', 21, 'CS'),
    ('10002', 'Rose', '女', 20, 'SE'),
    ('10003', 'Michael', '男', 21, 'IS'),
    ('10004', 'Hepburn', '女', 19, 'CS'),
    ('10005', 'Lisa', '女', 20, 'SE'),

]

for item in data:
    cursor.execute(sql, item)
connect.commit()
print('成功插入数据')
# 关闭数据库连接
connect.close()
