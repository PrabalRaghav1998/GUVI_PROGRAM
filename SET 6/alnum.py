import string
s1=string.ascii_letters
s2=string.digits
s=input()
if s in s1:
    if s in s2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
