n=int(input())
l=list(map(int,input().split()))
l.sort()
l1=[]
for i in range(1,n):
    if l[i]-l[i-1]!=0:
        l1.append(l[i]-l[i-1])
print(min(l1))

