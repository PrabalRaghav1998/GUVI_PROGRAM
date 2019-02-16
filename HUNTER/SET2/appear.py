n,k=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(set(l))
s1=l1[0]
for i in l1:
    s1=s1.intersection(i)
for i in s1:
    print(i,end=" ")
