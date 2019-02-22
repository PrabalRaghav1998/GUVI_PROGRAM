n1=int(input())
A=list(map(int,input().split()))
out1=[]
p=1
for i in A:
    p=p*i
for i in A:
    out1.append(p//i)
for i in out1:
    print(i,end=" ")
