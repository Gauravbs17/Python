m1=int(input("Enter marks of first test:"))
m2=int(input("Enter marks of second test:"))
m3=int(input("Enter marks of third test:"))

if m1<=m2 and m1<=m3:
    avgmarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avgmarks=(m1+m3)/2
elif m3<=m1 and m3<=m2:
    avgmarks=(m1+m2)/2

print("The average of best 2 test marks= ",avgmarks)