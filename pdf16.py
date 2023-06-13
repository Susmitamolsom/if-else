a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
if a==b and b==c:
    print("equilateral")
elif (a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b):
    print("isosceles")
else:
    print("scalene")