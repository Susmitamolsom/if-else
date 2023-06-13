a=int(input("enter classes"))
b=int(input("enter attenddance"))
per=a*b/100
if per>75:
    print("allowed to sit")
else:
    print("not allowed")