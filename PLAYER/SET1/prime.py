n,m=map(int,input().split())
a=list(range(n,m+1))
p=2
l=[]
while p<=m:
    for i in a:
        if i%p==0 and i!=p:
            a.remove(i)
    p+=1
print(len(a))
