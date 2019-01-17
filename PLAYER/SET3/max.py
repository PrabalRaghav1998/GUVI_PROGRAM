n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
for i in l1:
    l.append(i)
    print(max(l),end=" ")
