basic_salary=int(input("enter"))
if basic_salary<=10000:
    hra=basic_salary*20/100
    da=basic_salary*80/100
    g_salary=basic_salary+hra+da
    print(g_salary)
elif basic_salary<=20000:
    hra=basic_salary*25/100
    da=basic_salary*30/100
    g_salary=basic_salary+hra+da
    print(g_salary)
elif basic_salary>20000:
    hra=basic_salary*30/100
    da=basic_salary*95/100
    g_salary=basic_salary+hra+da
    print(g_salary)
else:
    print("none")