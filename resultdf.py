import pandas as pd
import numpy as np
ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}
ResultDF = pd.DataFrame(ResultSheet)
# print(ResultDF)
r=(ResultDF['Arnab']>90)
print(r)