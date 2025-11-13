n=int(input("Enter no of resistors: "))
a=int(input("Enter 1 for series and 2 for parallel: "))
l=[]
for i in range(n):
    b=float(input("Enter value of resistor"))
    l.append(b)

if a==2:
    s=0
    for i in l:
        s=s+(1/i)
    d=s**(-1)
    print("The equivalent resistance is:",d)

if a==1:
    s=0
    for i in l:
        s=s+i
    print("The equivalent resistance is:",s)