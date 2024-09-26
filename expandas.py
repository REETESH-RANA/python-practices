import pandas as pd
import numpy as np
# series is a one dimensional array with numeric index values from zero
# series1=pd.Series([1,2,3,4,5])
# print(series1)
# print()

# we can also assign user defined labels gto the indexes of any data types
# series2=pd.Series(["kavi","shyam","ravi"],index=[3,5,1])
# print(series2)
# print()
# we caan also use string or letter s as indices
# series2=pd.Series([2,3,4,5],index=["jan","feb","mar","april"])
# print(series2)
# print()

# we can also  create an series from one dimensional NUMPY array
# array1=np.array([1,2,3,4,5])
# series3=pd.Series(array1)
# print(series3)
# print()

# # we can create series from dictionary
# dict1={'India':'NewDelhi','UK':'London','Japan':'Tokyo'}
# print("dict1:",dict1)
# series8=pd.Series(dict1)
# print(series8)
# print()



# *************ACCESSING ELEMENTS OF Series***********
# now accessing elements of a series through indexes
# K = pd.Series(['NewDelhi','WashingtonDC', 'London', 'Paris'],
# index=['India', 'USA', 'UK', 'France'])
# print(K['India'])
# print()

# we can also access elements of series using the positional index
seriesCapCntry = pd.Series(['NewDelhi','WashingtonDC', 'London', 'Paris'],
index=['India', 'USA', 'UK', 'France'])
# print(seriesCapCntry[[1,3]])
# print()
# print(seriesCapCntry[['UK','USA']])
# print()

""" the index values associated with series can be altered with the index values"""
# seriesCapCntry.index=[10,20,30,40]
# print(seriesCapCntry)
# print()

" Accessing elements through slicing"
# print(seriesCapCntry[1:3])

"If labelled indexes are used for slicing"
# print(seriesCapCntry['USA' : 'France'])

# seriesAlph=pd.Series(np.arange(10,16,1),index=['a','b','c','d','e','f'])
# print(seriesAlph)
"accesing elements of a series"
# seriesAlph[1:3]=50
# print(seriesAlph)

# seriesAlph['c':'e']=500
# print(seriesAlph)

"""ATTRIBUTES  OF A SERIES"""
seriesCapCntry.name="Capitals" #NAME attribute assign a name to the series
# print(seriesCapCntry) 

seriesCapCntry.index.name='countries' #index.name attrinute assign index name 
# print(seriesCapCntry)
# print()

# # print(seriesCapCntry.values) #values attribute prints  a list values in series 
# print(seriesCapCntry.size)# print no. of values in the series object
# print()


# print(seriesCapCntry.empty) #print true if series is empty otherwise false
seriesEmpty=pd.Series() #creates an empty series
# print(seriesEmpty.empty)


""" head(n) : this attribute return first n members of series if value not passed thru n it takes default first 5"""
# print(seriesCapCntry.head(2))
# print(seriesEmpty.count())#it returns no of NaN values in a series
# print(seriesCapCntry.tail(1))#returns last n members of the series




# MATHEMATICAL OPERATIONS
# ADDITION
seriesA = pd.Series([1,2,3,4,5], index =['a', 'b', 'c', 'd', 'e'])
print(seriesA)
print()
seriesB = pd.Series([10,20,-10,-50,100],index = ['z', 'y', 'a', 'c', 'e'])
print(seriesB)
# seriesC=seriesA+seriesB
# print(seriesC) #output of addition is NaN if one of the elements or both elements have no value
# seriesd=seriesA.add(seriesB, fill_value=0)
# print(seriesd)


# SUBTRACTION
# seriesC=seriesA-seriesB # first method by using subtraction operator
# print(seriesC)

# seriesd=seriesA.sub(seriesB, fill_value=1000)#second method
# print(seriesd)

# Multiplication of two Series
# seriesC=seriesA * seriesB
# print(seriesC)
# seriesd=seriesA.mul(seriesB, fill_value=0)
# print(seriesd)

#  Division of two Series
# seriesC=seriesA/seriesB
# print(seriesC)
# seriesd=seriesA.div(seriesB, fill_value=0)
# print(seriesd)

# ppt pg no=26 complete with series dataframe topic is doone in dataframe.py


# Creation of an empty DataFrame
# dFrameEmt = pd.DataFrame()
# print(dFrameEmt)

'''Creation of DataFrame from NumPy ndarrays'''
# array1 = np.array([10,20,30])
# array2 = np.array([100,200,300])
# array3 = np.array([-10,-20,-30, -40])
# dFrame4 = pd.DataFrame(array1)
# print(dFrame4)

'''We can create a DataFrame using more than one ndarrays, '''
# dFrame5 = pd.DataFrame([array1, array3, array2], columns=[ 'A', 'B', 'C', 'D'])
# print(dFrame5)

#  Creation of DataFrame from List of Dictionaries
# Create list of dictionaries
# listDict = [{'a':10, 'b':20}, {'a':5,'b':10, 'c':20}]
# dFrameListDict = pd.DataFrame(listDict)
# print(dFrameListDict)

# Creation of DataFrame from Dictionary of Lists
# dictForest = {'State': ['Assam', 'Delhi','Kerala'], 'GArea': [78438, 1483, 38852] ,'VDF' : [2797, 6.72,1663]}
# dFrameForest= pd.DataFrame(dictForest)
# print(dFrameForest)
# print()
# '''We can change the sequence of columns in a DataFrame.
# This can be done by assigning a particular sequence of the dictionary keys as columns parameter, '''
# dFrameForest1 = pd.DataFrame(dictForest,
# columns = ['State','VDF', 'GArea'])
# print(dFrameForest1)
# print()

# Creation of DataFrame from Series Consider the following three Series:
# seriesA = pd.Series([1,2,3,4,5],index = ['a', 'b', 'c', 'd', 'e'])
# seriesB = pd.Series ([1000,2000,-1000,-5000,1000], index = ['a', 'b', 'c', 'd', 'e'])
# seriesC = pd.Series([10,20,-10,-50,100],index = ['z', 'y', 'a', 'c', 'e'])
# dFrame6 = pd.DataFrame(seriesA)
# print(dFrame6)
# dataframe using more than one series
# dFrame7 = pd.DataFrame([seriesA, seriesB])
# print(dFrame7)

# Creation of DataFrame from Dictionary of Lists
# DataFrames can also be created from a dictionary of lists. Consider the following dictionary consisting of the keys ‘State’, ‘GArea’ (geographical area) and ‘VDF’ (very dense forest) and the corresponding values as list.
# dictForest = {'State': ['Assam', 'Delhi','Kerala'],
# 'GArea': [78438, 1483, 38852] ,'VDF' : [2797, 6.72,1663]} 
# dFrameForest= pd.DataFrame(dictForest)
# print(dFrameForest)
# print()

# We can change the sequence of columns in a DataFrame. This can be done by assigning a particular sequence of the dictionary keys as columns 
# dFrameForest1 = pd.DataFrame(dictForest,
# columns = ['State','VDF', 'GArea'])
# print(dFrameForest1)

# Creation of DataFrame from Dictionary of Series
# ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
# 'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
# 'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
# 'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
# 'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}
# ResultDF = pd.DataFrame(ResultSheet)
# print(ResultDF)
# print()


# When a DataFrame is created from a Dictionary of  Series, the resulting index or row labels are a union of all  series indexes used to 
# create the DataFrame. For example:
# dictForUnion = { 'Series1' : pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e']) ,
# 'Series2' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']),
# 'Series3' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']) }
# dFrameUnion = pd.DataFrame(dictForUnion)
# print(dFrameUnion)
# print()

# When a DataFrame is created from a Dictionary of  Series, the resulting index or row labels are a union of all  series indexes used to 
# create the DataFrame. For example:
# dictForUnion = { 'Series1' : pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e']) ,
# 'Series2' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']),
# 'Series3' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']) }
# dFrameUnion = pd.DataFrame(dictForUnion)
# print(dFrameUnion)
# print()

"""Dictionary  of series """
dictformine = { 'Series1' : pd.Series([1,2,3,4,5,5,6,6],index=['a','b','c','d','e','f','g','h'])}
print(dictformine)
dframe=pd.Dataframe(dictformine)
# print(dframe)



