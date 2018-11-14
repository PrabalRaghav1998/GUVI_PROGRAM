n,m=map(int,input().split())
def lcm(n,m):
    if n>m:
        g=n
    else:
        g=m
    while g%n!=0 or g%m!=0:
        g+=1
    return g
print(lcm(n,m))
