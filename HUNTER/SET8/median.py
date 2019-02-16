n=int(input())
a=list(map(int,input().split()))
def f(l):
    if len(l)==0:
        return
    else:
        if len(l)%2==0:
            k=len(l)//2
            print((l[k-1]+l[k])//2)
            l.remove(l[k-1])
            l.remove(l[k-1])
            f(l)
        else:
            k=len(l)//2
            print(l[k])
            l.remove(l[k])
            f(l)
f(a)
