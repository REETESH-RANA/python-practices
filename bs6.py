#program to calculate simple intrest
p = int(input("enter the principal amount:"))
t = int(input("enter the time:"))
r = float(input("enter the rate of intrest:"))
simpleintrest = (p*t*r)/100
tot = "simple intrest of principle amount  %d is %d"%(p,simpleintrest)
print(tot)