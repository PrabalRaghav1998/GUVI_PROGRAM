from collections import Counter
s=input()
d=Counter(list(s))
m=max(d.values())
for i in d.keys():
    if d[i]==m:
        print(i)
        break
