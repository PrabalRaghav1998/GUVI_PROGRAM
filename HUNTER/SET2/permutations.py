from itertools import permutations
s=input()
l=list(permutations(s))
l1=[]
for i in l:
    n="".join(i)
    if n not in l1:
        print(n)
    l1.append(n)
