import pandas as pd
import numpy as np

data={
    'Name':['Alice','Bob',np.nan,'David','Emma'],
    'Age':[23,21,29,21,25],
    'Gender':['Female',np.nan,'Male','Male','Female'],
    'Weight':[65,58,61,63,59]
}
dataframe=pd.DataFrame(data)
print("===Original Dataset===")
print(dataframe)
df=dataframe.copy()
df['Gender']=df['Gender'].fillna(df['Gender'].mode())
print("===Dataframe after Replacement===")
print(df)