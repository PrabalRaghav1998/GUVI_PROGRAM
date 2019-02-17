n=int(input())
s=0
c=0
for i in str(n):
    k=int(i)
    s+=k**c
    c+=1
print(s)
