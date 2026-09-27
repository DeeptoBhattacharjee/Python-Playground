import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
df=pd.read_csv("Distance.csv")
df3=df.copy()
le=LabelEncoder()
df3['Category']=le.fit_transform(df3['Category'])
df3['Gender']=le.fit_transform(df3['Gender'])
print(df3)