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
cursor = connect.cursor()
# 执行SQL查询
cursor.execute("SELECT VERSION()")
# 获取单条数据
version = cursor.fetchone()
# 打印输出
print("MySQL数据库版本是：%s" % version)
# 关闭数据库连接
connect.close()