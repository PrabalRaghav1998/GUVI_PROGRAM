n=int(input())
p1=[]
for i in range(n):
    l=list(map(int,input().split()))
    p1.append(l)
res=[]
for i in range(n):
    for j in range(len(p1[i])):
        res.append(p1[i][j])
res=sorted(res)
for i in res:
    print(i,end=" ")
