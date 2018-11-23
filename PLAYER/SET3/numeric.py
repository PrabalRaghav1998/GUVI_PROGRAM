s=input()
k=0
for i in s:
    if i.isdigit():
        k=0
    else:
        k=1
        break
print("yes" if k==0 else "no")
