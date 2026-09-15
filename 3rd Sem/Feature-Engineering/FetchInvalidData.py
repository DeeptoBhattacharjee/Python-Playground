import pandas as pd
data={
    'Name':['ALice','Bob','Invalid Data','David','Emma'],
    'Gender':['Female','Male','Male','Male','Female'],
    'Age':[21,22,25,23,24]
}
df_org=pd.DataFrame(data)
print("===Original Dataset===")
print(df_org)
print()
df=df_org.copy()
print("Invalid Data:\n",df[df['Name']=='Invalid Data'])
