l=[]
s=input()
l.append(s)
while s!="":
    s=input()
    if s!="":
        l.append(s)
for i in l:
    print(int(eval(i)))
