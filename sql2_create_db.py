import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',  # 主机名
    port=3306,  # 端口号
    user='root',  # 数据库用户名
    passwd='123456',  # 密码
    db='test1',   # 数据库名称
    charset='utf8'  #编码格式
)
# 获取游标
#cursor = connect.cursor()
# 如果表存在，则先删除
#cursor.execute("DROP TABLE IF EXISTS student")
# 设定SQL语句
sql = """
 CREATE TABLE SC (
            Sno VARCHAR(10),
            Cno VARCHAR(10),
            Grade INT,
            PRIMARY KEY (Sno, Cno)
        );
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭数据库连接
connect.close()