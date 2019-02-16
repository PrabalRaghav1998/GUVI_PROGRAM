s=input()
j=0
k=0
for i in range(len(s)):
    if s[i]!=s[-(i+1)]:
        j=i
        k=i+1
        break
s1=s.replace(s[j],"")
s2=s.replace(s[-(k)],"")
if s1==s1[::-1] or s2==s2[::-1]:
    print("YES")
else:
    print("NO")
