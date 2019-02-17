n=int(input())
def p(n):
    k=1
    for i in range(2,n//2+1):
        if n %i==0:
            k=0
    return k
l=[]
for i in range(2,n//2+1):
    if p(i)==1:
        if p(n-i)==1:
            l.append((i,n-i))
print(min(l)[0],min(l)[1])
