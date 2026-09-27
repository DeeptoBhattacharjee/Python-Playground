from sklearn.preprocessing import MinMaxScaler
import numbers as np
import pandas as pd
data={
    'Age':[20,21,25,23,24],
    'Height':[172,183,167,181,175],
    'Weight':[65,70,68,67,72],
    'Grade':['A','B','A','A','B']
}
df_org=pd.DataFrame(data)
print("===Original Dataset===")
print(df_org)
df=df_org.copy()
print()
scaler=MinMaxScaler()
df[['Height','Weight']]=scaler.fit_transform(df[['Height','Weight']])
print("===Normalized Dataset===")
print(df)