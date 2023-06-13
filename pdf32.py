unit=int(input("enter"))
if unit<=100:
    print("no charge")
elif 100<unit<=200:
    amt=(unit-100)*5
    print(amt)
elif unit>100:
    amt=(unit-150)*10
    print(amt)
else:
    print("no bill")