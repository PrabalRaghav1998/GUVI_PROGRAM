n1=int(input())
s=input().split()
pre1=input()
l=len(pre1)
c=0
for i in range(n1):
    if(pre1==s[i][:l]):
        c=c+1
print(c)
