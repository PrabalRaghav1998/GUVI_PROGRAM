n=int(input())
l=list(map(int,input().split()))
for i in range(1,n+1):
    print(min(l[:i]),end=" ")
