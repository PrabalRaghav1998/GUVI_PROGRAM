import string
n=input()
c=0
s=string.punctuation
for i in n:
    if i in s:
        c+=1
print(c)
