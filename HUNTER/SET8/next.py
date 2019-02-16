n=int(input())
a=list(map(int,input().split()))
for i in range(0,n-1):
    if a[i+1]<a[i]:
        print(a[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1,end=" ")
