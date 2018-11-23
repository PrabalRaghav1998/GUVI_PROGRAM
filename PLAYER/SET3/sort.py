n=int(input())
l=input().split()
x=lambda x:len(x)
print(" ".join(sorted(l,key=x)))
