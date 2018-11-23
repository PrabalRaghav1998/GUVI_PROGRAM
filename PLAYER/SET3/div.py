n,k=map(int,input().split())
l=list(range(1,k+1))
l1=[]
for i in l:
    if n%i==0 and k%i==0:
        l1.append(i)
print(max(l1))
