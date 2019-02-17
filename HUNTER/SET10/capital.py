s=input()
i=0
j=0
while(j<len(s)):
    if s[j]!=' ':
        i+=1
    if i%2==1:
        print(s[j].upper(),end="")
    else:
        print(s[j],end="")
    j+=1
