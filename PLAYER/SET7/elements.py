n,k=map(int,input().split())
l=list(map(int,input().split()))
l.append(k)
l.sort()
i=l.index(k)
l1=l[:i]
for i in l1:
    print(i,end=" ")
