import pymysql

# 建立数据库连接
conn = pymysql.connect(host='localhost', user='root', password='123456', database='school')

# 创建游标对象
cursor = conn.cursor()

# 修改外键约束
sql = "ALTER TABLE SC DROP FOREIGN KEY sc_ibfk_1"
try:
    cursor.execute(sql)
    print("外键约束修改成功")
except Exception as e:
    print("修改外键约束失败:", str(e))

# 关闭游标和数据库连接
cursor.close()
conn.close()