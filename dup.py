#Checks for duplicates in a list and returns their indices.
#If more than one duplicate exists, it returns the indices of the one which has the smallest j-i value where j and i are the indices of the duplicate elements.
#And if still there is another duplicate pair then it returns the once which has the highest index value of i.
l=[]
n=int(input("Enter the number of inputs"))
for i in range(n):
    a=int(input("Enter the number"))
    l.append(a)
min=n+1
pair=()
for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            if (j-i)<=min:
                min=j-i
                pair=(i,j)
print("The indices of the duplicate element are:",pair)
