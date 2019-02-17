n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=l1 if k<n else l
l3=l if l2==l1 else l1
for i in l2:
    l3.append(i)
l3.sort()
for i in l3:
    print(i,end=" ")
