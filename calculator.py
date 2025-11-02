a=float(input("Enter first number"))

while True:
    
    
    c=input("Enter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division")
    if c!="+" and c!="-" and c!="*" and c!="/":
        break
    b=float(input("Enter next number"))
    if(c=="+"):
        a+=b
        
    if(c=="-"):
        a-=b
        
    if(c=="*"):
        a*=b
        
    if(c=="/"):
        a/=b
        
    
print("Final result:",a)
