def prime(n):
    c=0
    if n==1:
        return 1
    for i in range(2,n//2+1):
        if n%i==0:
            c=1
            break
    return c
n=int(input())
c=0
for i in range(2,n//2+1):
    if prime(i)==0:
        if prime(n-i)==0:
            c+=1
print(c)
