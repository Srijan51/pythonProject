l=[]
a=int(input("Enter the number of elements: "))
for i in range(a):
    x=int(input("Enter a number: "))
    l.append(x)

n=0
for i in range(a - 1):
    for j in range(a - 1 - i):
        s=0
        sn=0
        c=l[j]
        while c>0:
            n=c%10
            s=s+n
            c=c//10
        d=l[j+1]
        while d>0:
            n=d%10
            sn=sn+n
            d=d//10
        if s>sn:
            l[j],l[j+1]=l[j+1],l[j]

print("Sorted list is")
for i in range(a):
    print(l[i])