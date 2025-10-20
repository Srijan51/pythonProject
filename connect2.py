import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="1234",database="employee")
if mycon.is_connected():
    print("Successfully connected")
cursor=mycon.cursor()
cursor.execute("select * from emp;")
data=cursor.fetchall()
for row in data:
    print(row)
print("\n")
io=70000
st="select * from emp where salary>%s" %(io,)
cursor.execute(st)
data=cursor.fetchall()
for row in data:
    print(row)
str="insert into emp values(56,'lo', 38900,NULL)"
cursor.execute(str)
mycon.commit()
print("\n")
cursor.execute("select * from emp;")
data=cursor.fetchall()
for row in data:
    print(row)
