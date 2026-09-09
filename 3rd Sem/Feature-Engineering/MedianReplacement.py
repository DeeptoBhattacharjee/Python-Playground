import pandas as pd
import numpy as np

data={
    'Name':['Alice','Bob',np.nan,'David','Emma'],
    'Age':[23,21,29,np.nan,25],
    'Gender':['Female',np.nan,'Male','Male','Female'],
    'Weight':[65,58,np.nan,63,59]
}
dataframe=pd.DataFrame(data)
print("===Original Dataset===")
print(dataframe)
df=dataframe.copy()
df['Age']=df['Age'].fillna(df['Age'].median())
df['Weight']=df['Weight'].fillna(df['Weight'].median())
print()
print("===Dataset after Replacement===")
print(df)