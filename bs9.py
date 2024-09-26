# Write a program to find the number of and sum of all integers 
# greater than 100 and less than 200 that are divisible by 7.
i = 100
s = 0
while(i<=200):
    if(i%7==0):
        print(i,end=",")
        s=s+i
        i=i+1
    else:
        i=i+1

    # if(i==200):
    #     break
print("\nsum of no between 100 and 200 :",s)