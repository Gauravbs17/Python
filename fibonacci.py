#to generate particular fibonacci term in the series
def f(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return f(n-1)+f(n-2)
    
n=int(input("Enter a number:"))
if(n<0):
    print("Invalid inputs")
else:
    print("f(",n,")=",f(n),sep="")