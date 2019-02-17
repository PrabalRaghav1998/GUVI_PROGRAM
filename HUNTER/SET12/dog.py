n=int(input())
s=1
k=0
while s<=n:
    if s==n:
        k=1
        break
    s+=s
print("YES" if k==1 else "NO")
