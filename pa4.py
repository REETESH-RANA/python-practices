# Write code that classifies a given amount of money (which you store in a variable named amount), specified in cents,
# as greater monetary units. Your code lists the monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct),
# nickels (5 ct), and pennies (1 ct). Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies. The result is that you express the amount as the minimum number of coins needed.
amount = int(input("Enter the amount:"))
dollars = int(amount/100)
amount = amount-(dollars*100)
quarters = int(amount/25)
amount = amount-(quarters*25)
dimes = int(amount/10)
amount = amount-(dimes*10)
nickels = int(amount/5)
amount = amount - (nickels*5)
pennies = int(amount/1)
amount = amount-(pennies*1)
print("dollars:",dollars)
print("quarters:",quarters)
print("nickels:",nickels)
print("dimes:",dimes)
print("pennies:",pennies)
    
   

# coversion of cents into dollars,quarters,etc 