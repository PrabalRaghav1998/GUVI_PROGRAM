c=0
n=int(input())
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print("yes")
else:
    print("no") 
