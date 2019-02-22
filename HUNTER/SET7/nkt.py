from itertools import permutations
nkt1=list(map(int,input().split()))
l=list(map(int,input().split()))
n=nkt1[0]
k=nkt1[1]
t=nkt1[2]
p=permutations(l,k)
q=[]
for i in list(p):
    q.append(sum(i))
if(t in q):
    print('YES')
else:
    print('NO')
