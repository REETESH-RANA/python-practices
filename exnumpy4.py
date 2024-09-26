import numpy as np
import functools
l=np.array([1,3,5,2,2,2,5,5,7,8])
l.sort()
print(l)
unique,count=np.unique(l,return_counts=True)
m=(max(count))
for i in range(len(count)):
    if(m==count[i]):
        print(unique[i])

m=count.argmax() # it gives inndex of largest frequencies's index 
print(m)         # it gives inndex of minimum frequencies's index 