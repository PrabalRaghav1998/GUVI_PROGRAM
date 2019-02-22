n1=int(input())
l=list(map(int,input().split()))
p1=[]
f=0
for i in l:
    if(i not in p1):
        p1.append(i)
    else:
        f=1
        print(i)
        break
if(f==0):
    print("'unique'")
