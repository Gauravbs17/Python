n=5
num=0
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for j in range(i,0,-1):
        num+=1
        if num<10:
            print(num,end="  ")
        else:
            print(num,end=" ")
    print()
for i in range(2,n+1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for j in range(0,i):
        num-=1
        if num<10:
            print(num,end="  ")
        else:
            print(num,end=" ")
       
    print()