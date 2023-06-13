phy=int(input("enter"))
che=int(input("enter"))
bio=int(input("enter"))
math=int(input("enter"))
com=int(input("enter"))
total=phy+che+bio+math+com
per=total/500*100
if per>=90:
    print("grade A")
elif per>=80 and per<=90:
    print("grade B")
elif per>=70 and per<=80:
    print("grade C")
elif per>=60 and per<=70:
    print("grade D")
elif per>=40 and per<=60:
    print("grade E")
elif per<40:
    print("grade F")
else:
    print("fail")