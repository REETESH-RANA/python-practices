import numpy as np 
# L=[7,8,'9',5,4,8]
# print(L)
# A=np.array(L)
# print(A)
# # K=A*20
# print(A)

# TO MAKE ARRAY OF STRING DATATYPE
# L=[7,8,'9',5,4,8]
# print(L)
# A=np.array(L)
# print(A)

# L=[7,8,'9',5,4,8]
# print(L)
# A=np.array(L,dtype=int)
# print(A)
# # K=A*20
# print(A)

# to convert list of listinto array
# L=[[7,9,5],[3,6,3],[2,6,7]]
# print(L)
# A=np.array(L)
# print(A)

# ATTRIBUTES OF NUMPY
# P=[5,6,7,8]
# A1=np.array(P)
# L=[[4,5,6],[3,4,7],[6,8,9.0],[5,6,7]]
# A2=np.array(L)
# print(A1)
# print(A1.ndim) #ndim attribute show the dimension of array
# print(A1.shape)#it gives sequence of integers indicating size of array of each dimension
# print(A1.size)#it gives the totall elements of array
# print(A1.dtype)#it determine the datatype of the array elements
# print(A1.itemsize)#it specify the size in bytes of each element of the array ex: int32  32/8=4bytes.
# print("\n")

# print(A2)
# print(A2.ndim)
# print(A2.shape)
# print(A2.size)
# print(A2.dtype)



# OTHER METHODS OF CREATING NUMPY ARRAYS
# A=np.zeros(3,dtype='int32')
# print(A)
# A1=np.zeros((3,3) ,dtype='int32')
# print(A1)

array2=np.array([5,-2,3.3,'r'])
print(array2)

# to find the no of dimensions of a array we used ndarray.ndim attribute
print("dimension:",array2.ndim)

# to find shpe of array we use ndarray.shape
print("shape:"array2.shape)