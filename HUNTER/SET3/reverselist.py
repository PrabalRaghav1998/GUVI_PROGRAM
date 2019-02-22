n1=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
p1=[]
for i in l:
    p1.append(str(i))
print("->".join(p1))
