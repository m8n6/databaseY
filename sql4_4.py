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
INSERT INTO SC (Sno, Cno, Grade)
VALUES ('10005', '00004', 73);
""")
connect.commit()
print("添加成功！")
cursor.execute("""
SELECT Student.Sno, Student.Sname, Student.Sdept, Course.Cno, Course.Cname, SC.Grade
FROM Student
JOIN SC ON Student.Sno = SC.Sno
JOIN Course ON SC.Cno = Course.Cno
WHERE Student.Sno = '10005';
""")
result = cursor.fetchall()
for x in result:
  print(x)
connect.close()