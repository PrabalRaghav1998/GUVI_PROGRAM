n=input()
if n.isdigit():
    print("Yes")
else:
    try:
        k=float(n)
        print("Yes")
    except ValueError:
        print("No")
