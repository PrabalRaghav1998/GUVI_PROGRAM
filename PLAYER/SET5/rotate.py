n,k=input().split()
k=int(k)
l=list(n)
while k!=0:
    a=l.pop()
    l.insert(0,a)
    k-=1
print("".join(l))
