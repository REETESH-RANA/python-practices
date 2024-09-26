#Ask the user to enter three numbers. 
# Then print the largest, the smallest, and their average, rounded to 2 decimals

number1 = input("enter the first number:")
number2 = input("enter the second number:")
number3 = input("enter the third number:")
if(number1>number2 and number1>number3):
    if(number2>number3):
        stmnt=("%d is largest and %d is smallest"%(number1,number3))
elif(number2>number1 and number2>number3):
    if(number3>number1):
        stmnt = "%d is largest and %d is smallest"%(number2,number1)
else:
    print("number")
print(stmnt)