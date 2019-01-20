n=input()
s=""
while(len(n)!=""):
    p=n.index("0")
    l=n[:p+1]
    s+=" ".join(l)
    n.remove(l)
print(s)
