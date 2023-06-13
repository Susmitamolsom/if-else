u=int(input("enter"))
if u>=1 and u<=50:
    amount=u*0.50+20/100
    print(amount)
elif u>=50 and u<=151:
    amount=u*0.75+20/100
    print(amount)
elif u>=151 and u<=251:
    amount=u*1.20+20/100
    print(amount)
elif u>250:
    amount=u*1.50+20/100
    print(amount)
else:
    print("no fine")