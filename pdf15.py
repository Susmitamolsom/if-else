x=int(input("enter 1st no"))
y=int(input("enter 2nd no"))
z=int(input("enter 3rd no"))
if x+y>z and y+z>x and x+z>y:
    print("valid")
else:
    print("not valid")