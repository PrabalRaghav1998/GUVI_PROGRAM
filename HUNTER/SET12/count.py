l,r=map(int,input().split())
def prime(n):
    c=0
    if n==1:
        return 1
    for i in range(2,n//2+1):
        if n%i==0:
            c=1
            break
    return c
c=0
for i in range(l,r+1):
    if prime(eval("+".join(str(i))))==0:
        c+=1
print(c)
