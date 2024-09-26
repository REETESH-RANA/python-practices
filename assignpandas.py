import pandas as pd
import numpy as np

'''1]: create pandas dataframe'''
d={'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df=pd.DataFrame(d)
print(df)


'''2]:create and show dataframe from a specified dictionary with index labels'''

exam_data={'name':['Anatasia','Dimma','Katherine','James','Emily','Mathew','Laura','Kevin','Jonas','Michael'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels=['a','b','c','d','e','f','g','h','i','j']

df=pd.DataFrame(exam_data,index=labels,columns=['attempts','name','qualify','score'])
print(df)

'''3]. To display basic info specific dataframe and its data (using above dataframe)'''
# print("Summary of the basic information about this dataframe and its data")
# print(df.info()) 

'''4]. program to get first 3 rows of the dataframe'''
# d=df.iloc[:3,:4]
# print(d)

'''5].To select name and score column fromthe dataframe'''
# d=df.filter(items =['name','score'])
# print(d)

'''6].to select specified columns and rows from dataframe 'name','score' rows and 1,3,5,6 columns '''
# s=df.loc[0:,'name']          doubt
# print(s)


'''7]. select the rows where no   of attempts is greater then 2'''
# d=df[df['attempts']>2]
# print(d)
        
'''8].to count the number of row  and column'''
# d=df.shape
# d=df.shape[0]
# p=df.shape[1]
# print("number of rows",d)
# print("number of collumns",p)

'''9].to select the rows where the score is missing'''
# d=df[df['score'].isnull()]
# print(d)

'''10].to select the rows where the score is between 15 and 20'''
# d=df[(df['score']>=15) & (df['score']<=20)]   
# print(d)                    

'''11].To select number of rows where attempts is less than 2 and score greater than 15'''
# d=df[(df['attempts']<2) & (df['score']>15)]
# print(d)

'''12].write a program to change the score in row 'd' to 11.5'''
# df.loc['d','score']=11.5
# print(df)
'''13].to calculate the sum of examination attempts by students'''
# d=df['attempts'].sum()
# print("sum of attempts",d)

'''14].to calculate the mean of all students 'scores' '''
# d=df['score'].mean()
# print(d)
'''15]. to append a new row 'k' to dataframe  and now delete the new row and return to original dataframe '''
# df.loc['k']=[3,"rohit",'yes',45]
# print(df)

# df=df.drop('k',axis=0)
# print(df)

'''16].program to sort dataframe first by 'name' in descending order,then 'score' in ascending order''' 
# df=df.sort_values(by='name',ascending=False)
# df=df.sort_values(by='score')
# print(df)

'''17].replace the 'qualify' column  contains the values 'yes' and 'no' with "true" and "false" '''
# df=df.replace(to_replace=['yes','no'],value=['True','false'])
# print(df)

'''18].to change the name "james" to"suresh" in name column of the dataframe '''
# df=df.replace(to_replace="James",value="Suresh")
# print(df)        
'''19].to dlete attempts column from the dataframe'''
# df=df.drop("attempts",axis=1)
# print(df)
'''20].to insert new column in existing dataframe'''
# df['status']=["pass","fail",'pass','pass','pass','pass','pass','pass','fail','pass']
# print(df)
 
 
#         [pandas first assignment completed] 

'''21].program to iterate over rows in a dataframe'''
# for index, row in df.iterrows(): 
# for row in df.itertuples():
#  print(row,"\n")

'''22].to get list from dataframe column headers'''
# d=list(df.columns.values)
# print(d)

'''23].program to rename columns of a dataframe '''
# df=df.rename({'attempts':'col1','name':'col2','qualify':'col3','score':'col4'},axis=1)
# print(df)

'''24].program to select rows from a given dataframe based on values in some columns'''
#                      doubt


'''25].to change the order of a dataframe columns'''
# df=df.loc[:,['name','attempts','score','qualify']]
# d=df.iloc[:,[0,2,3,1]]
# print(d)

'''26].to add one row in an existing dataframe'''
# df.loc['k']=[3,"rohit",'yes',45]
# print(df)
 
'''27].to  write a dataframe to csv file using tab separator'''
# df=df.to_csv('output.csv',sep='\t',index=False)
# print(df)

'''28].to count city wise number of people froma given dataset(city,name of the person)'''
# data={
#     'name':['reet','kuldeep','janvi','ankit','keshav','rohit','rajveer','sonu','vikky',],
#     'city':['newdelhi','goa','mp','morena','mumbai','morena','goa','newdelhi','morena']
# }
# ds=pd.DataFrame(data)
# print(ds)
# d=ds.groupby(by=['city']).count()
# d=ds['city'].value_counts()
# print(d)

'''29].to delete a dataframe row based on given column value'''
# df=df.replace(np.nan,0)
# df=df[df.score != 0]   #filtering data in which sccore is not 0
# print(df)

'''30].to widen output display to see more columns'''
                        #   doubt

'''31].to select a row of series or dataframe by given integer index'''
# d=df.iloc[4]
# print(d)

'''32]. to replace all NaN values with zero's in a column of a dataframe '''
# df=df.replace(np.nan,0)
# df['score']=df['score'].replace(np.nan,0)
# print(df)



'''33].to convert an index into a column of a dataframe'''
# d=df.reset_index()
# df=df.reset_index(inplace=False)
# df=df.reset_index(level=)
# print(d)

'''34].to set  a given value for particular cell in dataframe using index value'''


'''35].to count the NaN values in one or more columns in dataframe'''
# d=(df['score'].isnull().sum())
# print("null values count:",d) 

'''36].to drop a list of rows from a specified dataframe'''
# df=df.drop(index=['b','d','g'],axis=0)
# print(df)

'''37].to reset index  in a given dataframe''' 
# d=df.reset_index()
# print(d)

'''38].program to devide a dataframe into given ratio'''
# df=pd.DataFrame(np.random.randn(10,2))
# print("original DataFrame:")
# print(df)
# part_70 = df.sample(frac=0.7,random_state=10)
# part_30 = df.drop(part_70.index)
# print("\n70% of the said  DataFrame:")
# print(part_70)
# print("\n30% of the said Dataframe:")
# print(part_30)

'''39]. to combining two series into a dataframe'''
# series1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# # print(series1)
# series2=pd.Series(['rohan','rajveer','reetesh','abbhay','monesh'],index=[10,20,30,40,50])
# # print(series2)
# df=pd.concat([series1,series2])
# print(df)


'''40].to shuffle a given dataframe rows'''
# df.sample(frac=1)
# print("\nNew DataFrame :\n",df)