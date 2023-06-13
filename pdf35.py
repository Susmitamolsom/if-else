cp=int(input("enter"))
if cp>100000:
    tax=15/100*cp
    print(tax)
elif cp>50000 and cp<=100000:
    tax=10/100*cp
    print(tax)
elif cp<=50000:
    tax=5/100*cp
    print(tax)
else:
    print("no tax")