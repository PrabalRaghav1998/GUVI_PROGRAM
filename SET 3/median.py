n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
print(k[len(k)//2])
