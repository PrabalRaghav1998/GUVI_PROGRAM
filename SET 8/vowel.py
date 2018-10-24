n=input()
v="aeiou"
k=0
for i in n:
    if i in v:
        k=1
        break
if k==1:
    print("yes")
else:
    print("no")
