from collections import Counter
n,k=map(int,input().split())
c=Counter(list(str(n)))
print(c[str(k)])
