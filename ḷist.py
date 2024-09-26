# to add total and percentage and pass /fail status students
# l=[[100,'peter',56,78,90],[200,'harry',90,90,90],[300,'alsia',55,66,77]]
# for s in l:
#     t=sum(s[2:])
#     s.append(t)
#     p=t/3
#     s.append(".1%f"%(p))
#     if(p>=60):
#         s.append("pass")
#     else:
#         s.append("fail")
# print(l)

# second method  for solving upper problem:
# for s in l:
#     t=sum(s[2:])
#     p=t/3
#     if(p>=60):
#         r=("pass")
#     else:
#         r=("fail")
#     s.extend([t,"%.1f"%(p),r])
# print(l)

# to filter names with kumar in any part
# l=['ram singh','deep kumar','ravi kumar','harry dutt','peter kumaranjan']
# f=[]
# for i in l:
#     if ("kumar" in i):
#         f.append(i)
# print(f)

# to print maximum produced crop its year and product name
# to print all data between two years 2001 - 2004
# year = ['2000','2001','2002','2003','2004','2005']
# food=['jawar','bajra','wheat','rice','ragi','corn']
# production=[300,4000,900,345,670,230]
# m=max(production)
# i=production.index(m)
# print(year[i],food[i],production[i])

# sy=int(input("enter the start year:"))                             fault have to correct from vedio
# ey=int(input("enter the end year:"))
# for v in range(year.index(sy),year.index(ey)+1):
#     print(year[v],food[v],production[v])


# find frequency of ages
age=[45,23,67,23,23,45,67,23,45,78,67]
age.sort()
print(age)
u=[]
for i in age:
    if(not i in u):
        u.append(i)
print(u)
for p in u:
    print(p,age.count(p))

