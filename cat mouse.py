c1=int(input("enter no"))
mouse=int(input("enter 1st "))
c2=int(input("enter 2nd"))
if c1<mouse and mouse>c2 and c1>c2:
    print(c1)
elif mouse>c2 and c1<mouse and c2>c1:
    print(c2)
elif c1==c2 and c2==mouse or c1==mouse:
    print(mouse)
else:
    print("none")