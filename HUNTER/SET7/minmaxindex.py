n=input()
l=list(map(int,input().split()))
m1=max(l)
mi1=min(l)
for i in range(len(l)):
    if(l[i]==mi1):
        print(i+1,end=" ")
for i in range(len(l)):
    if(l[i]==m1):
        print(i+1,end=" ")
