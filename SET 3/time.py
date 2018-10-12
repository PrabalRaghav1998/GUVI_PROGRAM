n=int(input())
d=n//60
if d!=0:
    n=n%(d*60)
print(str(d)+" "+str(n))
