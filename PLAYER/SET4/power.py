n=int(input())
m=n
c=0
while n!=0:
    n=n//2
    c+=1
if 2**(c-1)==m:
    print("yes")
else:
    print("no")
