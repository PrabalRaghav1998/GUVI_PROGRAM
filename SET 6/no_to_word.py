import inflect
p=inflect.engine()
n=int(input())
s=p.number_to_words(n)
print(s.capitalize())
