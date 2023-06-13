a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a<b and a<c and c>a and c>b:
    print(a,"is minimum",c,"is maximum")
elif a>b and a>c and c<a and c<b:
    print(a,"is maximum",c,"is minimum")
elif a<b and a<c and b>a and b>c:
    print(a,b)
elif a>b and a>c and b<a and b<c:
    print(a,b)
elif b<a and b<c and c>a and c>b:
    print(b,c)
else:
    print("no oldest no youngest")