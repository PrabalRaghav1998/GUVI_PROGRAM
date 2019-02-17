n=int(input())
l=[]
for i in range(n):
    l.append(input())
l.sort()
a,b=l[0],l[-1]
l1=[]
for i in range(len(a)):
    if a[i]==b[i]:
        l1.append(a[i])
    else:
        break
print("".join(l1))
