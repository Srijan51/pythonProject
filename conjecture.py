'''Start with any positive integer n.If n is even,
 the next number is n / 2.If n is odd, the next number is 3 times n + 1.
 Repeat this process until the number reaches 1.'''
def conjecture(n):
    c=0
    while n!= 1:
        c=c+1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    return c

a=int(input("Enter a positive integer: "))
result=conjecture(a)
print("The no of steps is:", result)
