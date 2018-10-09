n,m=map(int,input().split())
a=list(range(n+1,m))
for p in a:
    c=0
    for i in range(2,p):
        if p%i==0:
            c+=1
    if c==0:
        print(p,end=" ") 
