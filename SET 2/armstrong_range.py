n,m=map(int,input().split())
a=list(range(n+1,m))
for p in a:
    m=str(p)
    s=0
    for i in m:
        s+=int(i)**3
    if s==p:
        print(p,end=" ")
