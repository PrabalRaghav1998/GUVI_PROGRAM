import sys
n1=int(input())
l=list(map(int,input().split()))
max=max2=99999999999
for i in l:
    if i<max:
        max2=max
        max=i
    elif i<max2 and i>max:
        max2=i
print(max2)
