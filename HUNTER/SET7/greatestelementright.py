n1=int(input())
l=list(map(int,input().split()))
p=[0]*n1
for i in range(n1-1):
    p[i]=max(l[i+1:n1])
p[-1]=0
for i in p:
    print(i,end=" ")
