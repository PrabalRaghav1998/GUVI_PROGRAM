n,k=map(int,input().split())
l=list(range(k,n*k+1))
l1=[]
for i in l:
    if i%n==0 and i%k==0:
        l1.append(i)
print(min(l1))
