#to check Similarity b/w 2 strings
str1=input("Enter string1:\n")
str2=input("Enter string2:\n")
if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str1)
    long=len(str2)
matchcnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchcnt+=1
print("Similarity between two said strings:")
print(matchcnt/long)
