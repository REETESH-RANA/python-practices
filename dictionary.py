# d={'9833838322':'harry singh','98978968768':'peter kumar','9809899987':'alia kumari'}
# print(type(d))
# pn=input("enter the mobile no: ")
# print(d[pn])
# d['9999988888']='Tony singh'
# print(d)
# d['9833838322']='Tony singh'
# del d['9999988888']
# print(d)

# d={'9833838322':['harry singh','jaipur'],'98978968768':['peter kumar','pune'],'9809899987':'alia kumari'}
# print(d['9833838322'][1])


# d={'9833838322':{'name':'harry singh','city':'jaipur'},'98978968768':{'name':'peter kumar','city':'pune'},'9809899987':{'name':'alia kumari','city':'noida'}}
# print(d['9833838322']['name'])

'''d={'9833838322':{'name':'harry singh','city':'jaipur'},'98978968768':{'name':'peter kumar','city':'pune'},'9809899987':{'name':'alia kumari','city':'noida'}}
k=d.keys()
k=list(d.keys())
print(k)
print(k[0])
for k in d.keys():
    print(k)'''


# v=d.values()
# print(v)
# for i in d.values():
#     print(i)


# for reading items
# print(d.items())
# for i in d.items():
    # print(i)
    # print(i[0],i[1])


    # setdefault(key,value)
# d={'9833838322':{'name':'harry singh','city':'jaipur'},'98978968768':{'name':'peter kumar','city':'pune'},'9809899987':{'name':'alia kumari','city':'noida'}}
# d['9833838322']['state']='Rajasthan'
# d['9833838322'].setdefault('state','Rajasthan') for appending it doesn't over write any value
# print(d)
# r=d.get('983383832','record not found')    by using get function
# print(r)

# r=d.pop('9833838322')
# print(d)

# r=d.popitem()
# print(d)

# creating dictionary from static method
# r=dict.fromkeys(['BJP','INC','AAP','SP','BSP'],0)
# print(r)

# d1={'9833838322':{'name':'harry singh','city':'jaipur'},'98978968768':{'name':'peter kumar','city':'pune'},'9809899987':{'name':'alia kumari','city':'noida'}}
# d2={'9833838342':{'name':'vishal dua','city':'new delhi'},'98978968668':{'name':'anamika kaapoor','city':'noida'},'9809899987':{'name':'desh deepak','city':'banglore'}}
# d1.update(d2)
# print(d1)