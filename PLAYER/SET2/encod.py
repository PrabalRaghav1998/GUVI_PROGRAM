s=input()
s1=""
for i in s:
    p=ord(i)
    if p==122:
        p=96
    if p==90:
        p=64
    p=p+3
    s1+=chr(p)
print(s1)
