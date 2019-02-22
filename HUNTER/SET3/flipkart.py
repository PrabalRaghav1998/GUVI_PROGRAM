n1=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
m=1
for i in range(n1-1):
    for j in range(i+1,n1):
        if(s[j]>=f[i]):
            i=j
            m=m+1
            break
    if(i==n1-1):
        break
print(m)
