a,b=map(int,input().split())
def swap(a,b):
    a=a-b
    b=a+b
    a=b-a
    print(str(a)+" "+str(b))
swap(a,b)
