# -NumPy is a Python library used for working with arrays.
# -It also has functions for working in domain of linear algebra, fourier transform,
#  and matrices.
# -NumPy was created in 2005 by Travis Oliphant.
# -It is an open source project and you can use it freely. 
# -NumPy stands for Numerical Python.
# -we can install it from commandar by writting "pip install NumPy"


'''                         QUESTION 4
                      **********************
'''

import numpy as np
a=np.zeros((1,10))
print(a)
b=np.array(['a','e','i','o','u'])
print(b)
c=np.ones((2,5),dtype=int)
print(c)
myarray1=np.array([[2.7,-2,-19,3,4],
          [0.3,4,99.9,43,54],
          [10.6,0,13,34,21]])
print(myarray1)
startvalue=4
step_size=4
endvalue=startvalue+3*5*step_size

myarray2=np.arange(startvalue, endvalue , step_size ,dtype=float).reshape((3,5))
print(myarray2)

print(myarray1.ndim,myarray2.ndim,b.ndim,a.ndim,c.ndim)

print(myarray1.shape,myarray2.shape,b.shape,a.shape,c.shape)


print(myarray1.size,myarray2.size,b.size,a.size,c.size)


print(myarray1.dtype,myarray2.dtype,b.dtype,a.dtype,c.dtype)


print(myarray1.item,myarray2.item,b.item,a.item,c.item)


print(myarray1.itemsize,myarray2.itemsize,b.itemsize,a.itemsize,c.itemsize)

print(b[2],b[3])
print(myarray1[2],myarray1[1])

print(b[::-1])

print(c/3)


w=np.array(myarray1+myarray2)
print(w)

newarray=np.array(myarray1-myarray2)
print(newarray)

# newarray1=np.array(myarray2 @ myarray2)
# print("matrix multiplication",newarray1)

print(myarray1/myarray2)

import math
x=np.sqrt(myarray2)
m=x/2
print("",m)

# arr=np.power(myarray1,3)
# result_arr=(arr/2)
# print(result_arr)

'''              QUESTION 7
             *****************
'''
print(myarray2)
trans=np.transpose(myarray2)
print(trans)

print(b[::-1])

n=myarray1.min(axis=1)
print(n)

'''               QUESTION 8
'''
myarray2A,myarray2B,myarray2C,myarray2D,myarray2E=np.split(myarray2,5,axis=1)
print("myarray2A",myarray2A)
print("myarray2B",myarray2B)
print("myarray2C",myarray2C)
print("myarray2D",myarray2D)
print("myarray2E",myarray2E)

# zerosA,zerosB,zerosC,zerosD=np.split(a,[2],[5],[7],[8])
# print(zerosA)
# print(zerosB)
# print(zerosC)
# print(zerosD)



start_value=-1
stepsize=0.25
end_value=start_value+14*3*stepsize
myarray4=np.arange(start_value,end_value,stepsize).reshape(14,3)
print(myarray4)


sums=np.sum(myarray4)
print(sums)


sumrow=np.sum(myarray4,axis=1)
print("row wise summing of elements",sumrow)


sumcol=np.sum(myarray4,axis=0)
print("column wise summing of elements",sumcol)

minele=np.min(myarray4,axis=1)
print(minele)

maxele=np.max(myarray4)
print(maxele)

means=np.mean(myarray4,axis=1)
print("mean of each row",means)

stdcol=np.std(myarray4,axis=0)
print(stdcol)