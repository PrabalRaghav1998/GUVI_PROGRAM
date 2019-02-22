m=input().split('#')
n=input().split('#')
s1=0
p=0
for i in range(3):
    s1 =s1+int(m[i+1])
    p=p+int(n[i+1])
if(s1>p):
    print(m[0])
if(p>s1):
    print(n[0])
