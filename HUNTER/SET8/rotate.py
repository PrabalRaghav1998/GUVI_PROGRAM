n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    a=l.pop(0)
    l.append(a)
l=map(str,l)
print(" ".join(l))
