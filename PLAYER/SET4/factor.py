n=int(input())
l=[]
for i in range(2,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if i%2==0:
        print(i,end=" ")
