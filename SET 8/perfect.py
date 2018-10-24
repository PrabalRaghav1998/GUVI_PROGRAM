import math
l,r=map(int,input().split())
p=l*r
s=int(math.sqrt(p))
print("yes" if s*s==p else "no")
