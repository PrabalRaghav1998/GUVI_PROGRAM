import sys
def diff(a,b):
    return b-a
l=[]
n,m=map(int,input().split())
while True:
    l.append((n,m))
    try:
        n,m=map(int,input().split())
    except ValueError:
        break
for i in l:
    print(diff(i[0],i[1]))
