s1,s2=input().split()
n=min(len(s1),len(s2))
s=""
for i in range(n):
    s+=s1[i]
    s+=s2[i]
st=s2 if len(s2)>len(s1) else s1
c=1
for i in range(n,len(st)):
    if st==s2:
        s+=str(c)
        s+=st[i]
    if st==s1:
        s+=st[i]
        s+=str(c)
    c+=1
print(s)
