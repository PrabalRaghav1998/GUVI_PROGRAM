n=int(input())
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(n))
