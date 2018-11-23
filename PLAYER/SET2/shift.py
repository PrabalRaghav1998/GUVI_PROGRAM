n,k=map(int,input().split())
l=list(map(int,input().split()))
while k!=0:
    p=l.pop(len(l)-1)
    l.insert(0,p)
    k-=1
print(l)
