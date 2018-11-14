s=input()
s1,s2="",""
for i in range(0,len(s)):
    if i%2==0:
        s1+=s[i]
    else:
        s2+=s[i]
print(s1+" "+s2)
