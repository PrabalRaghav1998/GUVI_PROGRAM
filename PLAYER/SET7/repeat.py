from collections import Counter
n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=Counter(l)
for i,j in l1.items():
    if j==k:
        print(i)
        break
