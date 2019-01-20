a,b=input().split()
s1=set(a)
s2=set(b)
if len(s1 & s2)>0:
    print("yes")
else:
    print("no")
