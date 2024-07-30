'''
 1 2 3 4 5 
  6 7 8 9
   0 9 0
    9 0
     9
    0 9
   0 9 0
  9 8 7 6
 5 4 3 2 1 
'''

n=5
num=0
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for j in range(i,0,-1):
        num+=1
        if num<=9:
            print(num,end=" ")
        else:
            if(num%2==0):
                print(0,end=' ')
            else:
                print(9,end=' ')
           
    print()
for i in range(2,n+1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for j in range(0,i):
        num-=1
        if num<=9:
            print(num,end=" ")
        else:
            if(num%2==0):
                print(0,end=' ')
            else:
                print(9,end=' ')
       
    print()