time=float(input("enter time"))
if time>=7.00 and time<=9.00:
    print("breakfast")
elif time>=9.00 and time<=12.30:
    print("1st coding")
elif time>=12.30 and time<=15.00:
    print("lunch time")
elif time>=15.00 and time<=17.00:
    print("2nd coding")
elif time>=18.00 and time<=20.00:
    print("English class")
else:
    print("more class")