per=int(input("enter"))
if per>80:
    print("grade A")
elif per>60 and per<=80:
    print("grade B")
elif per>50 and per<=60:
    print("grade C")
elif per>45 and per<=50:
    print("grade D")
elif per>25 and per<=45:
    print("grade E")
elif per<25:
    print("grade F")
else:
    print("fail")