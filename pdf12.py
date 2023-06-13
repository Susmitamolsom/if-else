month=input("enter")
if month=="jan" or month=="march" or month=="may" or month=="july" or month=="aug" or month=="oct"or month=="dec":
    print("31st days")
elif month=="april" or month=="june" or month=="september":
    print("30th days")
else:
    print("28th days")