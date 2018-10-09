n=int(input())
m=str(n)
s=0
for i in m:
    s+=int(i)**3
if s==n:
    print("yes")
else:
    print("no")
