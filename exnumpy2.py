import numpy as np

# ATTRIBUTES of numpy
# arithmetic operations elemtwise sum in two arrays
# A1=np.array([4,5,6,7])
# A2=np.array([10,20,30,40])
# A3=A1+A2
# print(A3)

# for matrix multiplication
# A3=A1@A2
# print(A3)

# transpose and shape of array
# A1=np.array([[4,5],[6,7],[6,9],[3,4]])
# print(A1.shape)
# A2=A1.transpose()
# print(A2.shape)
# print(A2)

# A1=np.array([[4,5],[6,7],[6,9],[3,4]])
# A1.sort()
# print(A1) 
# column wise sorting
# A1=np.array([[14,5,1],[1,60,7],[4,6,9],[2,13,4]])
# A1.sort(axis=0)
# print(A1) 
# row wise sorting
# A1=np.array([[14,5,1],[1,60,7],[4,6,9],[2,13,4]])
# A1.sort(axis=1)
# print(A1) 

# concatenation of arrays
# A1=np.array([4,5,6,7,8,9])
# A2=np.array([8,7,5])
# A3=np.concatenate((A1,A2),dtype='float')
# print(A3)

# vertically merge by conatenation
# A1=np.array([[14,5,1],[1,60,7],[4,6,9],[2,13,4]])
# A2=np.array([[4,4,4],[5,5,5]])
# A3=np.concatenate((A1,A2),axis=0)
# print(A3)
# row-wise merging using concatenation
# A1=np.array([[14,5,1],[1,60,7]])
# A2=np.array([[4,4,4],[5,5,5]])
# A3=np.concatenate((A1,A2),axis=1)
# print(A3)

# reshaping
# A=np.array([1,2,3,4,5,6,7,8,9])
# b=A.reshape(3,3)
# print(b)
 