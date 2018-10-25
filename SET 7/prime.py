c=0
n=int(input())
for i in range(1,n):
    if n%i==0:
        c+=1
if c==1:
    print("yes")
else:
    print("no") 
