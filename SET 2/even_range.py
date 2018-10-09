n,m=map(int,input().split())
a=(list(range(n+2,m,2)) if n%2==0 else list(range(n+1,m,2)))
for i in a:
    print(i,end=" ")
