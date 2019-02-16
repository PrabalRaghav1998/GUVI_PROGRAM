n=int(input())
l=list(map(int,input().split()))
m1=l[0]
m2=l[0]
p=l[0]
for i in range(1,n):
    if l[i]<0:
        t=m1
        m1=m2
        m2=t
    m1=max(l[i],m1*l[i])
    m2=min(l[i],m2*l[i])
    p=max(p,m1)
print(p)
