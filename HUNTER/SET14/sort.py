n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
for i in range(n//2):
    print(l1[-(i+1)],end=" ")
    print(l1[i],end=" ")
if n%2==1:
    print(l1[n//2])
