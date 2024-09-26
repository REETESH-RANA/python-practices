#  The cover price of a book is $24.95, but bookstores get a 40 percent discount.
#   Shipping costs $3 for the first copy and 75 cents for each additional copy.
#   Calculate the total wholesale costs for 60 copies.
cover_price=24.95
each_copy = 0.75
first_copy=3
total_cost = (first_copy+cover_price)+(each_copy*59)
print(total_cost)