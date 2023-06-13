age=int(input("enter age"))
sex=input("enter sex")
nd=int(input("enter"))
if age>=18 and age<=30 and sex=="m":
    amount=nd*700
    print(amount)
elif age>=18 and age<=30 and sex=="f":
    amount=nd*750
    print(amount)
elif age>=30 and age<=40 and age=="m":
    amount=nd*800
    print(amount)
elif age>=30 and age<=40 and sex=="f":
    amount=nd*850
    print(amount)
else:
    print("no amount")