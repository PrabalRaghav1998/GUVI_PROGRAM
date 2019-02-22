n1=int(input())
l=list(map(int,input().split()))
uv1=list(map(int,input().split()))
u=uv1[0]
v=uv1[1]
p=[]
q=[]
r=[]
for i in range(n1):
    if(l[i]==u):
        p.append(i)
    if(l[i]==v):
        q.append(i)
for i in p:
    for j in q:
        if(i-j>0):
            r.append(i-j)
        if(j-i>0):
            r.append(j-i)
print(min(r))
