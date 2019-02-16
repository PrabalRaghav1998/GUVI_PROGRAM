n=int(input())
l=list(map(int,input().split()))
l1=[max(l)]
c=l.index(max(l))
for i in range(c+1,n):
    k=l[i+1:]
    if l[i]>max(k):
        l1.append(l[i])
for i in l1:
    print(i,end=" ")
print()
print(max(l))
