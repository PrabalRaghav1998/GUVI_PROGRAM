from collections import Counter
l=[]
s=input()
l.append(s)
while s!="":
    s=input()
    if s!="":
        l.append(s)
c1,c2=0,0
for i in l:
    c=Counter(i)
    if c["("]==c[")"]:
        print("yes")
    else:
        print("no")
