n=int(input())
a,b=1,1
print(str(a)+" "+str(b),end=" ")
n-=2
while n!=0:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n-=1
