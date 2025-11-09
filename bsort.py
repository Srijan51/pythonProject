l1=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    l1.append(ele)

for i in range(0,n):
    for j in range(0,n-i-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
            
print("Sorted list is: ")
for i in range(0,n):
    print(l1[i])