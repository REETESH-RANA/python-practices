# all()
# checks wheather all elements are non zero/not null 
# if yes then it will return true otherwise false

# t=(1,1,1,0,56,1,4)
# k=all(t)
# print(k)


# t=('peter','','Vishal','alia')
# k=any(t)#checks data are non or present
# print(k)

t=((1,2,3),(4,5,6,8),(6,7,8,9))
# for v in t:
#     for i in v:
#      print(i,end=" ")

#     print()

# reading of tuple by using indexing method
# t=((1,2,3),(4,5,6,8),(6,7,8,9))
# for i in range (len(t)):
#     for j in range(len(t[i])):
#         print(t[i][j],end=" ")
#     print()

# t=((1,2,3),(4,5,6,8),(6,7,8,9))
# y=((1,2,3),(4,5,6,8),(6,7,8,9))
# z=()
# for i in range (len(t)):
#     temp=()
#     for j in range(len(t[i])):
#         s=t[i][j]+y[i][j]
#         temp+=(s,)
#     z+=(temp,)
# print(z)

t=(('pepsi',89),('fanta',67),('frooti',100),('limca',60),('redbull',120))
# for i in range(len(t)):
#     for j in range(len(t[i])):
#         if(t[i][j]<70):
#         # if(j[0]<70):
            # print(i)  

# for p in t:
#     if(p[1]<70):
#         print(p)

# search for element starts with f
# for p in t:
#     if(p[0].startswith("f")):
#         print(p)

#  search for element 
name=input("enter the product: ")
found=False
for p in t:
    if(p[0]==name):
        print(p)
        found=True
        break

if(not found):
    print("product not found")

