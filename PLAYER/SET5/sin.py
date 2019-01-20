import math
s=math.sin(math.radians(int(input())))
if s==1.0 or s==0 or s==-1.0 or s==-0:
    print(int(s))
else:
    print(round(s,2) if s!=0 or s!=1 else int(s))
