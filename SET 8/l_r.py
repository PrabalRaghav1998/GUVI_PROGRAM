n=int(input())
l,r=map(int,input().split())
l1=list(range(l+1,r))
print("yes" if n in l1 else "no")
