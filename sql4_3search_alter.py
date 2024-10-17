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
UPDATE Course
SET Credit = 5
WHERE Cno = '00001' AND Cname = 'DataBase';
""")
print("修改成功！")
cursor.execute("""
SELECT Cno,Cname, Credit
FROM Course
WHERE Cno = '00001';
""")
result = cursor.fetchone()
print(result)
connect.close()