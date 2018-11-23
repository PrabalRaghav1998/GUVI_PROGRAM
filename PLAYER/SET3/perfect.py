import math
n,k=map(int,input().split())
l=list(range(n,k+1))
c=0
for i in l:
    s=math.sqrt(i)
    if i==s**2:
        c+=1
print(c)
