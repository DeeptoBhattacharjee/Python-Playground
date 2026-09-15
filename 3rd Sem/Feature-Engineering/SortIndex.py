import pandas as pd
data={
    'Name':['ALice','Bob','Invalid Data','David','Emma'],
    'Gender':['Female','Male','Male','Male','Female'],
    'Age':[21,22,25,23,24]
}
df_org=pd.DataFrame(data)
df=df_org.copy()
df=df[df['Name']!='Invalid Data']
df.loc[2]=['Eliza','Female',26]
print("===Dataset before Sorting===")
print(df)
print()
print("===Dataset after Sorting===")
print(df.sort_index())