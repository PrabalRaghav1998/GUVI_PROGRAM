nq1=list(map(int,input().split()))
n=nq1[0]
q=nq1[1]
l=list(map(int,input().split()))
r=[]
out1=[]
for i in range(q):
    p=list(map(int,input().split()))
    r.append(p)
for i in range(q):
    out1.append((l[r[i][0]-1:r[i][1]]))
for j in range(q):
    res=out1[j][0]
    for i in range(len(out1[j])-1):
        res=res^out1[j][i+1]
    print(res)
