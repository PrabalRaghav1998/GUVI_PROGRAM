n=int(input())
if n%4==0:
    if n%400==0 or n%100!=0:
        print("yes")
    else:
        print("no")
else:
    print("no")
