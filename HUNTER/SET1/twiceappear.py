n1=int(input())
l=list(map(int,input().split()))
l=sorted(l)
for i in range(n1):
    c=l.count(l[i])
    if(c==2):
        i=i+2-1
    else:
        print(l[i])
        break
