val=int(input("Enter the value:"))
str_val=str(val)
if str_val==str_val[::-1]:
    print("Entered value is a palindrome")
else:
    print("Entered value is not a palindrome")

count=0
for i in range (0,10):
    if str_val.count(str(i))>0:
        print("The character ",str(i)," appears ",str_val.count(str(i))," number of times")
