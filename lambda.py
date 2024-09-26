#  L=[36,84,65,67,70]
# grade=lambda L:list( 'a' if(i>=80 and i<=100) else "b" if(i>=60 and i<=79)else "c" if(i>=40 and i<=59) else "d" for i in L)
# k=grade(L)
# print(k)

# a simple sum program using reduce function in lambda python
'''l=[2,3,4,5,7,6]
import functools
def call(a,b):
    return(a+b)
k=functools.reduce(call,l)
print(k)'''


''''a program to calculate total amounts and total offers'''
# import functools
# def TotalAmount(a,b):
#     return a+b[1]
# def TotalOffer(a,b):
#     return a+b[2]

# l=[['Sony LED',60000,55000],['LG TV',45000,40000],['LG WM',25000,19000]]
# TA=functools.reduce(TotalAmount,l,0)
# TO=functools.reduce(TotalOffer,l,0)
# print("total amount:",TA)
# print("offer amount:",TO)
# print("you saved:",TA-TO)


########################################################################
###########          exception handling          #######################
'''try:
    v=float(input("enter any value:"))
    d=float(input("enter another value:"))
    c=v/d
    print("devision: ",c)
except ZeroDivisionError as e:
    print("devision should not be zero ")
except ValueError as e:
    print("error: enter float value only..")
finally:
    print("good bye")'''

# creating a progroom of exception handling using modules that we have created in mylib 
'''from mylib import input_int
x=input_int("enter rate :")
y=input_int("enter quantity :")
z=x*y
print("amount:",z)'''

# for  taking input only  string or raising exception
'''from mylib import input_str
k=input_str("enter your name: ")'''