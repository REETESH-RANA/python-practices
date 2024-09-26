rate=float(input("enter the rate:"))
quantity=float(input("enter the quantity:"))
amount = rate * quantity
if(amount>10000):
  discount=amount*20/100
  gst=amount*12/100
else:
  discount=amount*5/100
  gst=amount*8/100
print("total:",amount)
print("discount:",discount)
print("gst:",gst)
Totalamount = (amount+gst)-discount
print("Total amount:",Totalamount)
