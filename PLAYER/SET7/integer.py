n=int(input())
for i in range(1,n+1):
    if n%i==0:
        p=n//i
        if p%2==1:
            print(i)
            break
