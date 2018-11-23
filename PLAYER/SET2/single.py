from collections import Counter
n=int(input())
l=list(map(int,input().split()))
d=Counter(l)
m=min(d.values())
for i in d.keys():
    if d[i]==m:
        print(i)
        break
