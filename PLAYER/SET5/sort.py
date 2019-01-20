n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
if l==l1:
    print("yes")
else:
    print("no")
