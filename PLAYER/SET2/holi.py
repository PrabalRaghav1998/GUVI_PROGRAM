l=[]
s=input()
l.append(s)
while s!="":
    s=input()
    if s!="":
        l.append(s)
h=["Saturday","Sunday"]
for i in l:
    if i in h:
        print("yes")
    else:
        print("no")
