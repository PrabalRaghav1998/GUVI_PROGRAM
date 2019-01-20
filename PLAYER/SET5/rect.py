import math
p,a=map(int,input().split())
p=p/2
try:
    s=math.sqrt(p**2-4*1*a)
except ValueError:
    s=0
x1=p+s/2
x2=p-s/2
if x1.is_integer() or x2.is_integer():
    print("yes")
else:
    print("no")
