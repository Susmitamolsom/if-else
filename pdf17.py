a_cost=int(input("enter"))
s_cost=int(input("enter 2nd no"))
if a_cost-s_cost>0:
    print("loss")
elif s_cost-a_cost>0:
    print("profit")
else:
    print("no loss no profit")