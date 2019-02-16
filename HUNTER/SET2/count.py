n,k=map(int,input().split())
def p(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
x=0
for i in range(n,k+1):
    b=bin(i)[2:]
    c=b.count("1")
    if(p(c)==1):
        x+=1
print(x)
