import numpy as np 
import pandas as pd

ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, -91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, -71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}
DF = pd.DataFrame(ResultSheet)
# copy
# NF=DF.copy() #it will make copy of  whole dataframe

# RANK
# NF=DF.rank(method="first",ascending=False) # it gives rank  by default each col
# NF=DF.rank(axis=1,ascending=False) # for column wise
# NF=DF.rank(axis=0,ascending=False)# for row wise rank finding
# print(NF)

# SORT VALUES
# NF=DF.sort_values(by='Riya')# for sortunh
# NF=DF.sort_values(by=['Riya','Arnab']) # for sorting multiple columns
# NF=DF.loc[:,['Arnab']].sort_values(by='Arnab',ascending=False) 
# print(NF)

# SORT_INDEX()
# print(DF)
# NF=DF.sort_index()
# NF=DF.sort_index(ascending=False)

# iterrows()
# result=DF.iterrows()
# for t in result:
#     print(t)

# iteritems()
# result=DF.items()
# print(result)
# for(name,data) in result:     
#     print(name,data)

'''NOTE: ASCENDING=True/False
            used with rank/sort_values/sort_index
        AXIS=0/1
            used with RANK
'''

# print(DF)
# NF=DF.abs() #it will change neg values into positive values
# print(NF)


# ARIITHMETIC OPERATIONS
# s1=pd.Series([4,5,6,7])
# s2=pd.Series([10,20,30,40])
# s3=s1.add(s2)
# print(s3)
# s3=s1+s2
# print(s3)

# s3=s1.cummax()
# print(s3)

s1=pd.Series([90,57,45,78])
s2=s1.where(s1>50,other=-1) #here -1 will replace NaN Value with a value you  specified in other
print(s2)
s1.where(s1>50)