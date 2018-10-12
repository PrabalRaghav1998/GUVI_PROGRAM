n=int(input())
l=list(map(int,input().split()))
c=[0]*(max(l)+1)
b=[0]*len(l)
for i in range(0,len(l)):
    c[l[i]]+=1
for i in range(1,max(l)+1):
    c[i]=c[i]+c[i-1]
for i in range(len(l)-1,-1,-1):
    b[c[l[i]]-1]=l[i]
    c[l[i]]-=1
for i  in b:
    print(i,end=" ")
