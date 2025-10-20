a=float(input("Enter first number"))

for i in range(0,9999):
    
    
    c=input("Enter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division")
    if c!="+" and c!="-" and c!="*" and c!="/":
        break
    b=float(input("Enter next number"))
    if(c=="+"):
        a+=b
        continue
    if(c=="-"):
        a-=b
        continue
    if(c=="*"):
        a*=b
        continue
    if(c=="/"):
        a/=b
        continue
    
print("Final result:",a)
