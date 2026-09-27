import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv("Distance.csv")
print("===Original Dataset===\n",df)
cols=['Distance(km)']
df_selected=df[cols]
print()
print("===Extracted Columns Preview===")
print(df_selected)
plt.figure(figsize=(6,4))
plt.hist(df['Distance(km)'],bins=10)
plt.title('Histogram of Distance(km)')
plt.xlabel('Distance(km)')
plt.ylabel('Frequency')
plt.show()