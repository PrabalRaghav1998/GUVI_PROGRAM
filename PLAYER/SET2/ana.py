from collections import Counter
d=Counter(list("kabali"))
n=int(input())
l=[]
for _ in range(n):
    l.append(input())
c=0
for i in l:
    k=0
    d1=Counter(list(i))
    if d==d1:
        c+=1
print(c)
