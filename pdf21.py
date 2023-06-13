quantity=int(input("enter"))
total_cost=quantity*100
if total_cost>1000:
    discount=total_cost*10/100
    total_cost=total_cost-discount
    print(total_cost)
else:
    print("no discount")