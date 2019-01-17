n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=0
u=len(l)-1
k1=0
while l1<=u:
    m=(l1+u)//2
    if l[m]==k:
        k1=1
        break
    if l[m]<k:
        l1=m+1
    if l[m]>k:
        u=m-1
if k1==1:
    print("yes")
else:
    print("no")
