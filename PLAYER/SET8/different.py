n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
if len(l1)==1:
    print(l1[0])
if len(l2)==1:
    print(l2[0])
