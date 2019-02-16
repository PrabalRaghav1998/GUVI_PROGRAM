n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k=0
while True:
    a=l.pop(0)
    l.append(a)
    k+=1
    if l==l1:
        break
print(k)
