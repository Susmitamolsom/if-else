year_service=int(input("enter"))
salary=int(input("enter salary"))
if year_service>5:
    bonus=salary/100*5
    total_salary=salary+bonus
    print(total_salary)
else:
    print("no bonus")