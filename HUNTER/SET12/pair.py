n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    for j in range(i,n):
        if a[i]<a[j]:
            c+=1
print(c)
