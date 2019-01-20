n,k=map(int,input().split())
c,m=0,n
while(n!=0):
    n=n//k
    c+=1
print("yes" if k**(c-1)==m else "no")
