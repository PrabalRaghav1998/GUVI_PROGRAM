n,m=map(int,input().split())
a=list(range(n,m+1))
p=2
l=[]
while p<=m:
    a=[a=a.remove(i) for i in a if i%p==0]
    p+=1
print(len(a))
