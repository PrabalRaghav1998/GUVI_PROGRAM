n=int(input())
l=list(map(int,input().split()))
s=set(l)
print(2*sum(s)-sum(l))
