a=[]
n=int(input("Enter value of n:"))
print("Enter array elements:")
for i in range (n):
    x=int(input())
    a.append(x)

for i in range(5):
    if a[i+0]==a[i+1]:
        print(a[i+2])
        break
    elif a[i+1]==a[i+2]:
        print(a[i+0])
        break
    elif a[i+0]==a[i+2]:
        print(a[i+1])
        break