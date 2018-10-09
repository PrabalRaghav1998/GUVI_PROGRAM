n=input()
n=n.lower()
vowels=['a','e','i','o','u']
if ord(n)>=97 and ord(n)<=122:
    print("Vowel" if n in vowels else "Consonant")
else:
    print("invalid")
