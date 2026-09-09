import pandas as pd
import numpy as np

data={
    'Name':['Alice','Bob',np.nan,'David','Emma'],
    'Age':[23,21,29,np.nan,25],
    'Gender':['Female',np.nan,'Male','Male',np.nan]
}
dataframe=pd.DataFrame(data)
print("The Null Count:-")
print(dataframe.isnull().sum())
