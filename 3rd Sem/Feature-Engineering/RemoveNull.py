import pandas as pd
import numpy as np

data={
    'Name':['Alice','Bob',np.nan,'David','Emma'],
    'Age':[23,21,29,np.nan,25],
    'Gender':['Female',np.nan,'Male','Male','Female']
}
dataframe=pd.DataFrame(data)
print("===Original Dataset===")
print(dataframe)
df=dataframe.copy()
print("===Datatset after Removal===")
print(df.dropna())