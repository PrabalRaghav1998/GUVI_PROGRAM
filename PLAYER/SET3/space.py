import re
s1=input()
l=s1.split(" ")
l1=[]
for i in range(0,len(l)):
    if l[i]=="" and i<len(l):
        if l[i+1]=="":
            continue
        l1.append(l[i])
    else:
        l1.append(l[i])
s2=""
for i in l1:
    if i=="":
        s2+=" "
        continue
    s2+=i
print(s2)
