a=int(input("eneter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
if a>b and c<a:
    print(a)
elif b>c and a<b:
    print(b)
elif c>b and a<c:
    print(c)
else:
    print("none")