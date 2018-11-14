l=[]
s=input()
l.append(int(s))
while s!="":
    s=input()
    if s!="":
        l.append(int(s))
def div(n):
    if n%2!=0:
        return n
    else:
        return div(n//2)
for i in l:
    print(div(i))
