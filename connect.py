import mysql.connector as sqlt
mycon=sqlt.connect(host="localhost",user="root",passwd="1234",database="employee")
if mycon.is_connected():
    print("Successfully connected mysql")
cursor=mycon.cursor()
cursor.execute("select * from emp")
data=cursor.fetchall()
for row in data:
    print(row)
print("\n")
st="select * from emp where salary>50000"
cursor.execute(st)
da=cursor.fetchall()
for row in da:
    print (row)
print("\n")
a=int(input("Enter id"))
b=input("Enter name")
c=float(input("Enter salary"))
st1="insert into emp values({},'{}',{})".format(a,b,c)
cursor.execute(st1)
mycon.commit()
mycon.close()
