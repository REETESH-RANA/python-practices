'''1. Write a Python script to sort (ascending and descending) a dictionary by value.   '''
# k={"India":"New delhi","China":"Beijijng","Shri lanka":"Columbo","Bangladesh":"Dhaka"}
# t=list(k.items())
# print(t)
# i=0
# while(i<len(t)):
#     j=0
#     while(j<(len(t)-1)-i):
#         if(t[j][1]>t[j+1][1]):
#             L=t[j]
#             t[j]=t[j+1]
#             t[j+1]=L
#         j=j+1
#     i=i+1
# print(t)
# K=dict(t)
# print(K)

'''2. Write a Python script to add a key to a dictionary. '''
# d=dict()
# d={0: 10, 1: 20}
# d.setdefault(2,30)
# print(d)

'''3. Write a Python script to concatenate following dictionaries to create a new one.   '''
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# d=dict()
# d.update(dic1)
# d.update(dic2)
# d.update(dic3)
# print(d)

'''4. Write a Python script to check if a given key already exists in a dictionary.   '''
# dic1={1:10,2:20,3:30,4:40}
# k=1
# if k in dic1:
#     print("key exist in dict")
# else:                                 doubt
#     print("key doesn't exist")

'''5. Write a Python program to iterate over dictionaries using for loops.   '''
# dic1={1:10,2:20,3:30,4:40}
# for i in dic1.items():
#     print(i)

'''6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).'''   
# d={}
# n=int(input("enter the limit:"))
# for i in range(1,n):
#     d.setdefault(i,i*i)
# print(d)

'''7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are square of keys'''
# d={}
# for i in range(1,16):
#     d.setdefault(i,i*i)
# print(d)

'''8. Write a Python script to merge two Python dictionaries.   '''
# dic1={1:10,2:20,3:30,4:40}
# dic2={'a':'apple','b':'bada apple','c':'chota apple'}
# dic1.update(dic2)
# print(dic1)

'''9. Write a Python program to iterate over dictionaries using for loops.   '''
# dic={'a':'apple','b':'bada apple','c':'chota apple'}
# for i in dic.items():
#     print(i)

'''10.Write a Python program to sum all the items in a dictionary.   '''
# dic1={1:10,2:20,3:30,4:40}
# s=0
# r=sum(dic1)
# for i in dic1.values():
#     s=s+i
# print(s)
# print('sum of all items in dict is ',r+s)

'''11. Write a Python program to multiply all the items in a dictionary.'''
# dic={1:10,2:20,3:30,4:40}
# m=1
# for i in dic.values():
#     m=i*m
# print("multipy of all item in dic is ",m)

'''12. Write a Python program to remove a key from a dictionary.   '''
# dic={1:10,2:20,3:30,4:40}   
# dic.pop(3)
# print(dic)

'''13. Write a Python program to map two lists into a dictionary. '''
# l1=['hell','loop','worst','pain','death']
# l2=['1','2','3','4','5']  
# d=dict(zip(l1,l2))
# print(d)

'''14. Write a Python program to sort a dictionary by key. '''
# dic={14:10,9:20,5:30,2:40}   
# for i in dic.keys():                 doubt

'''15. Write a Python program to get the maximum and minimum value in a dictionary.   '''
# dic={14:10,9:20,5:30,2:40}   
# m=max(dic.values())
# print(m)
# print(min(dic.values()))

'''16. Write a Python program to get a dictionary from an object's field'''        
# dic={1:10,9:20,5:30,2:40,'a':['hell','loop'],'b':['boot','reboot']}
# for i in dic.values():
#     if(isinstance(i,list)==True):
#         print(i) 

# dic = {1: 10, 9: 20, 5: 30, 2: 40, 'a': ['hell', 'loop'], 'b': ['boot', 'reboot']}
# for key, value in dic.items():
#     if isinstance(value, list):
#         print(key, ":", value)


'''17. Write a Python program to remove duplicates from Dictionary'''
# dic={14:10,9:20,5:30,2:40,3:40}
# print(dic)
# l=[]
# for i  in dic.values(): 
#     l.append(i)
# print("list of values:",l)
# l=set(l)
# print("removed duplicates from values",l)

'''18. Write a Python program to check a dictionary is empty or not.'''   
# dic={14:10,9:20,5:30,2:40,3:40}
#one method
#  count=0
# for i in dic.keys():
#     count=count+1
# if(count==0):
#     print("dictionary is empty")
# else:
#     print("not empty")

# second method
# if(len(dic)==0):
#     pritn("empty")
# else:
#     print("not empty")

'''19. Write a Python program to combine two dictionary adding values for common keys. '''  
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# k=list(d1.keys())+list(d2.keys())
# k=list(set(k))
# d3={}
# print(k)
# for k in k:
#     a=d1.get(k,0)
#     b=d2.get(k,0)
#     if(a!=0 and b!=0):
#         d3[k]=a+b
#     elif(a!=0):
#         d3[k]=a
#     elif(b!=0):
#         d3[k]=b
# print(d3)

'''20. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}'''
# d={}
d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

        

'''21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.'''   
# S={'1':['a','b'], '2':['c','d']}
            # doubt
            
'''30. Write a Python program to get the top three items in a shop.   '''
# d= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# i=0
# while(i<3):
#     p=max(d.values())           doubt
#     k=d.pop(p)
#     print((p))
#     i=i+1
# print(d)


'''31. Write a Python program to get the key, value and item in a dictionary. '''
# dic={1:10,2:20,3:30,4:40}   
# for key,value in dic.items():
#     print('key :',key,'value :',value)
#     print('item',(key,value))
#     print()


'''32. Write a Python program to print a dictionary line by line. '''
# dic={14:10,9:20,5:30,2:40,3:40}
# for i in dic.items():
#     print(i)

'''33. Write a Python program to check multiple keys exists in a dictionary'''
# dic={14:10,9:20,5:30,2:40,3:40}
# s=[]
# for i in dic.keys():
#     if(i in dic):
#         print('yes multiples key existed')
#     else:
#         print("not existed")    doubt
# print(i)        

'''34. Write a Python program to count number of items in a dictionary value that is a list.'''   
# dic={14:10,9:[10,20],5:[3,0],2:40,3:40}
# count=0
# for i in dic.values():
#     if(isinstance(i,list)==True):
#         count=count+1    
# print(count)

