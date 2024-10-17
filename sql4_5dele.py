import pymysql.cursors
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='school',
    charset='utf8'
)
cursor = connect.cursor()
cursor.execute("""
DELETE FROM Student WHERE Sno = '10003';
""")
connect.commit()
cursor.execute("""
DELETE FROM SC WHERE Sno = '10003';
""")
connect.commit()
print("删除成功！")
connect.close()