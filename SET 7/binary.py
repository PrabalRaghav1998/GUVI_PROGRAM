n=input()
k=0
s="01"
for i in n:
    if i in s:
        k=0
    else:
        k=1
        break
if k==1:
    print("no")
else:
    print("yes")
