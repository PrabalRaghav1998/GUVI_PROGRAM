n=int(input())
l,l1=[],[]
for i in range(2,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        l1.append(i)
for i in l1:
    print(i,end=" ")
