n=input()
c=0
i=0
while(i<len(n)-1):
    if n[i]=='a' and n[i+1]=='b':
        c+=2
        i+=2
    elif n[i]=='b':
        c=0
        i+=1
    i+=1
if n[-1]=='a':
    c+=1
print(c)
