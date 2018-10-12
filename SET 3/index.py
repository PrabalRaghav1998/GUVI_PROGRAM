n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(str(i)+" "+str(l.index(i)))
