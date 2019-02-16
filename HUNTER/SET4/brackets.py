n=int(input())
def f(s,p,n,o,c):
    if(c==n):
        for i in s:
            print(i,end="")
        print()
        return
    else:
        if(o>c):
            s[p]='}'
            f(s,p+1,n,o,c+1)
        if(o<n):
            s[p]='{'
            f(s,p+1,n,o+1,c)
s=[""]*2*n
f(s,0,n,0,0)
