n,m=input().split()
c=0
for i,j in zip(n,m):
    if i!=j:
        c+=1
if c==1:
    print("yes")
else:
    print("no")
