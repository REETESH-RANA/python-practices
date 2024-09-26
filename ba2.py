#program to enter length and breadth and find its perimeter and area
length = int(input("enter the length of the rectangle:"))
breadth = int (input("enter the breadth of the rectangle:"))
perimeter = (2*length) + (2*breadth)
area = length*breadth
print(perimeter)
print("area of rectangle is ",area)