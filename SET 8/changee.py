s=input()
l=len(s)
if l%2!=0:
    n=s[:l//2]+"*"+s[l//2+1:]
    print(n)
else:
    n=s[:l//2-1]+"*"+"*"+s[l//2+1:]
    print(n)
