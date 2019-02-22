n1=int(input())
l=list(map(int,input().split()))
for i in range(n1):
    if(l[i]%2==0 and i%2!=0):
        print(l[i],end=" ")
    if(l[i]%2!=0 and i%2==0):
        print(l[i],end=" ")
