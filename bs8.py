# An electric power distribution company charges its domestic consumers as follows.Consumption Units Rate of Charge
# 0-200 Rs.0.50 per unit
# 201-400 Rs.100 plus Rs.0.65 per unit 
# 401-600 Rs.230 plus Rs.0.80 per unit .
# Write a C program that reads the customer number and power consumed and prints the amount to be paid by the customer

customer_num = int(input("Enter the customer number:"))
consumed_power = float(input("Enter the power consumed by consumer:"))

if((consumed_power >=0) and (consumed_power <= 200)):
    total_amount = consumed_power * 0.50 
elif(consumed_power >= 201 and consumed_power <= 400):
    total_amount = 100 + (consumed_power * 0.65)
elif(consumed_power >= 401 and consumed_power <= 600):
    total_amount = 230 + (consumed_power * 0.80)
else:
    print("enter the valid unit....")

Bill = ("Customer's number :\t%d\nPower unit consumed:\t%d\n\t\t----------------\nAmount to be paid:\t%.2f"%(customer_num,consumed_power,total_amount))
print(Bill)