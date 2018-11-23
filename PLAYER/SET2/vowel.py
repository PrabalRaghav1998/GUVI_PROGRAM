s=input()
for i in s:
    if i in "aeiouAEIOU":
        s=s.replace(i,"")
print(s[::-1])
