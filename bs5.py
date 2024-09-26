#finding third angle of a triangle
i=1
while(i<=2):
    a = int(input("enter the first angle of triangle:"))
    b = int(input("enter the second angle of triangle:"))
    c = 180-(a+b)
    print("third angle of the triangle is:",c)
    i+=1