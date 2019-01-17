from collections import Counter
n=input()
c=Counter(n.lower())
m=min(c.values())
for i in c.keys():
    if c[i]==m:
        print(i,end=" ")
