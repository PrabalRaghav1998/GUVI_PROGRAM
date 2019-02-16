n=int(input())
l=list(map(int,input().split()))
l.sort()
i=0
j=n-1
a=i
b=j
m=999999999999999
while i<j:
    s=l[i]+l[j]
    if abs(s)<abs(m):
        m=s
        a=i
        b=j
    if s<0:
        i+=1
    else:
        j-=1
print(l[b],l[a])
