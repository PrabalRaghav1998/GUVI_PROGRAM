n=int(input())
l=list(str(n))
s=0
for i in l:
    s+=int(i)
s1=str(s)[::-1]
if str(s)==s1:
    print("YES")
else:
    print("NO")
