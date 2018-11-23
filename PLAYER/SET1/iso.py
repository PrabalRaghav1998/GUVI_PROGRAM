a,b=input().split()
if len(a)!=len(b):
    print("no")
d={}
k=0
if len(a)==len(b):
    for i,j in zip(a,b):
        if i in d and d[i]!=j:
            d[i]=[d[i]]+[j]
        else:
            d[i]=j
for i in d.keys():
    if len(d[i])>1:
        k=1
        break

print("yes" if k==0 else "no")
