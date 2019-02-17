n=int(input())
l=list(map(int,input().split()))
l.append(n)
l.sort()
i=l.index(n)
l1=l[:i]
for i in l1:
    print(i,end=" ")
