import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="1234",database="employee")
if mycon.is_connected():
    print("Succesfully connected")
cur=mycon.cursor()
query="select * from emp where salary>50000"
cur.execute(query)
data=cur.fetchall()
for i in data:
    print(i)
