#The cost of one type of mobile service is Rs.250 plus Rs.1.25 for each call made over and above 100 calls. 
#Write a program to read calls made and print the bill for  customer.
call=int(input("enter the total calls made:"))
mobservice=250
eachcall=1.25
if(call>100):
    extracallcharges = (eachcall*call)
    bill=(mobservice + (eachcall*call))
else:
    extracallcharges = 0
    bill=(mobservice)

print("Bill:\ntotal calls made:\t%d\nmobile service charge:\t%d\nExtra call charges:\t%d\n\t--------------------\n\t\t\t%d"%(call,mobservice,extracallcharges,bill))