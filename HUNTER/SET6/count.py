n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
i=0
j=0
c=0
while j<n:
    if l[j]-l[i]==k:
        c+=1
        i+=1
        j+=1
    elif l[j]-l[i]>k:
        i+=1
    else:
        j+=1
print(c)
