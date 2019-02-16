s=input()
l=s.split()
c=0
for i in l:
    if c%2==0:
        print(i[::-1],end=" ")
    else:
        print(i,end=" ")
