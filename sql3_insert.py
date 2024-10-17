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
sql = "INSERT INTO SC (Sno, Cno, Grade) VALUES (%s, %s, %s)"
data = [
            ('10002', '00003', 86),
            ('10001', '00002', 90),
            ('10002', '00004', 70),
            ('10003', '00001', 85),
            ('10004', '00002', 77),
            ('10005', '00003', 88),
            ('10001', '00005', 91),
            ('10002', '00002', 79),
            ('10003', '00002', 83),
            ('10004', '00003', 67)
        ]

for item in data:
    cursor.execute(sql, item)
connect.commit()
print('成功插入数据')
# 关闭数据库连接
connect.close()
