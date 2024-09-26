import numpy as np 
import  pandas as pd


# Creation of DataFrame from Dictionary of Series
ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}
ResultDF = pd.DataFrame(ResultSheet)
# print(ResultDF)
# print()

""""OPERATIONS ON ROWS AND COLUMNS IN DATA FRAMES
Adding a new column to a dataframe and """
# ResultDF['Preeti']=[34,55,87]
# print(ResultDF)

'''if that  column name already exist then it will update  their values also we can  change the entire column to a particular value'''
# ResultDF['Ramit']=[99,98,78]
# ResultDF['Arnab']=90
# print(ResultDF)

'''if we want  to add a new row  to our dataframe then'''
# ResultDF.loc['English']=[86,86,98,99,76,77]
# print(ResultDF)
# '''we cannot create  a new row with a name which is already exist this will update the existed values '''
# ResultDF.loc['English']=0
# print(ResultDF)

'''we can set all values of a DataFrame to a particular value, for example:'''
# ResultDF[:]=0 #it set all values to zero
# print(ResultDF)

'''if we want to delete a row or a column from  a  dataframe
we use Dataframe.drop[] method'''
# ResultDF=ResultDF.drop('Ramit',axis=1) #axis  = 0 for row and 1 for column
# print(ResultDF)

'''RENAMING ROW LABELS OF A DATAFRAME WE USE DATAFRAME.rename() '''
# ResultDF=ResultDF.rename({'Maths':'sub1','Science':'sub2','English':'sub3','Hindi':'sub4'},axis='index')
# print(ResultDF)
# renaming column labels
# ResultDF=ResultDF.rename({'Arnab':'student1','Ramit':'studennt2','samridhi':'student3','Riya':'student4','Mallika':'student5','Preeti':'student6'},axis='columns')
# print(ResultDF)


# ACCESING ELEMENTS USING INDEXES
'''when a single column is passed it returns result as a series'''
# print(ResultDF.loc[:,'Arnab'])
# print()
# print(ResultDF['Arnab'])
# print(ResultDF.loc[['Science','Hindi']])

# ACCESSING ELEMENTS BY BOOLEAN INDEXING: it result in true and false
# print(ResultDF.loc['Maths']>90)
# print(ResultDF.loc[:,'Arnab']>90)

# ACCESSING  DATAFRAME ELEMENTS THRU SLICING 
# print(ResultDF.loc['Maths':'Science']) 
# print(ResultDF.loc['Maths':'Science','Arnab'])
# print(ResultDF.loc['Maths':'Science','Arnab':'Samridhi'])
# print(ResultDF.loc['Maths':'Science',['Arnab','Samridhi']])
# ResultDF.loc['Maths','Ramit':'Riya':1]=1000
# print(ResultDF)

# JOINING ,MERGING AND CONCATENATION OF DATAFRAMES
dframe1=pd.DataFrame([[1,2,3],[4,5],[6]],columns=['c1','c2','c3'],index=['r1','r2','r3'])
print(dframe1)
print()
dframe2=pd.DataFrame([[10,20],[30],[40,50]],columns=['c2','c5'],index=['r4','r2','r5'])
print(dframe2)

dframe1=dframe1.add(dframe2)
print(dframe1)