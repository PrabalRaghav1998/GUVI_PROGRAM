s1=input()
f=k=a=d=e=0
for i in range(len(s1)):
    if(s1[i]=='@'):
        a=a+1
        j=i
        if(j>2):
            k=1
    if(s1[i]=='.'):
        d=d+1
        if(i-j>=5):
            f=1
    if(s1[-3:]=='com'):
        e=1
if(a==1 and k==1 and d==1 and f==1 and e==1):
    print('YES')
else:
    print('NO')
