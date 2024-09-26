'''1. Write a Python program to create a set'''
# k=set([12,23,23,42,42])
# print(k)
# # or alternate method
# k=dict()
# print(k)

''' 2. Write a Python program to iteration over sets. '''
# k={45,43,32,'helll'}
# for i in k:
#     print(i)

''' 3. Write a Python program to add member(s) in a set.''' 
# k={54,21,23,876,442,32}
# s=input("enter the item you want to insert in set:")
# k.add(s)
# print(k)

'''4. Write a Python program to remove item(s) from set   '''    
# k={54,21,23,876,442,32}
# k.remove(876)
# print(k)

'''5. Write a Python program to remove an item from a set if it is present in the set.'''    
# k={54,21,23,876,442,32}
# j=set()
# v=input("enter the item you want to delete from set: ")
# for i in k:
#     j+=i
#     if(i==v):
#         k.remove(i)
# print(k)                      doubt


'''6. Write a Python program to create an intersection of sets.   '''    
# k={54,21,23,876,442,32}
# j={22,20,33,12,876,32,54}
# s=k.intersection(j)
# print('intersection:',s)

''' 7. Write a Python program to create a union of sets. '''
# k={54,21,23,876,442,32}
# j={22,20,33,12,876,32,54}
# s=k.union(j)
# print('intersection:',s)

'''8. Write a Python program to create set difference.    '''   
# k={54,21,23,876,442,32}
# j={22,20,33,12,876,32,54}
# s=k.difference(j)
# print('difference:',s)

'''9. Write a Python program to create a symmetric difference. '''
# k={54,21,23,876,442,32}
# j={22,20,33,12,876,32,54}
# s=k^j  #those elements which are in k and j but not present in both sets
# print(s)

'''10. Write a Python program to issubset and issuperset.'''       
# k={22,20,33,12,876,32,54}
# j={22,32,54}
# s=j.issubset(k) #if j is subset of k
# l=k.issuperset(j)#if k is superset of j
# print('j is subset of k:',s)
# print('k is superset of j:',l)

'''11. Write a Python program to create a shallow copy of sets. '''
# k={22,20,33,12,876,32,54}
# j=k.copy()
# print(k)
# print(j)

'''12. Write a Python program to clear a set. '''
# k={22,20,33,12,876,32,54}
# s=k.clear()
# print(k)
# print(s)

'''14. Write a Python program to find maximum and the minimum value in a set.'''     
# k={22,20,33,12,876,32,54}  
# num=0
# for i in k:
#     if(i>num):
#         num=i
# # print(num)
# print(max(k))
# print(min(k))
    
'''15. Write a Python program to find the length of a set.'''       
# k={22,20,33,12,876,32,54}
# count=0
# for i in k:
#     count+=1
# print('length of the set:',count)
