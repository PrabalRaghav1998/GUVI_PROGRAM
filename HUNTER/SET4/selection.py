n=int(input())
l=list(map(int,input().split()))
l1=l
def f(l):
    if len(l)==1:
        print(l1.index(l[0]))
    else:
        l=l[1:len(l):2]
        f(l)
f(l)
