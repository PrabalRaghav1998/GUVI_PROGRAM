l=[]
s=input()
l.append(s)
while s!="":
    s=input()
    if s!="":
        l.append(s)
for i in l:
    s=set(i)
    if len(s)<len(i):
        print("No")
    if len(s)==len(i):
        print("Yes")
