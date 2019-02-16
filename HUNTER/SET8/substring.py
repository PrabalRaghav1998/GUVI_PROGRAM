s,n=input().split()
n=int(n)
for i in range(0,len(s)-n+1):
    print(s[i:i+n],end=" ")
