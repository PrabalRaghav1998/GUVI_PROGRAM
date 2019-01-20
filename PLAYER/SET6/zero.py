n1=int(input())
l=list(map(int,input().split()))
l=l[::-1]
i=l.index(0)
for j in range(2,n1):
    if l[j]!=0:
        print(l[j],end=" ")
