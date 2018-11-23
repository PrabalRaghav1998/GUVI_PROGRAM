s2=input()
s=list(s2)
s1=""
for i in range(len(s)-1):
    if i%2==0:
        t=s[i]
        s[i]=s[i+1]
        s[i+1]=t
    s1+=s[i]
s1+=s[len(s)-1]
print(s1)
