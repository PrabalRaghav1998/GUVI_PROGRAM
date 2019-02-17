n=int(input())
def p(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
if n<=2:
    print(0)
else:
    for i in range(2,n):
        if p(i)==True:
            print(i,end=" ")
