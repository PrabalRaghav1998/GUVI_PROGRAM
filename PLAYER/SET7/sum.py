n,k=map(int,input().split())
l=list(map(int,input().split()))
i=0
j=n-1
l.sort()
c=0
while i<j:
    if l[i]+l[j]==k:
        c=1
        break
    elif l[i]+l[j]>k:
        j-=1
    else:
        i+=1
print("yes" if c==1 else "no")
