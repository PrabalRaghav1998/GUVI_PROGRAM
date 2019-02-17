n=int(input())
l=list(map(int,input().split()))
c=1
l1=[]
for i in range(1,n):
    if l[i]>l[i-1]:
        c+=1
    else:
        l1.append(c)
        c=1
l1.append(c)
print(max(l1))
