import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv("Distance.csv")
df1=df.copy()
df1['Distance_Log']=np.log(df1['Distance(km)'])
print(df1[['Distance(km)','Distance_Log']])
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(df1['Distance(km)'],bins=10)
plt.title('Original Distance')
plt.subplot(1,2,2)
plt.hist(df1['Distance_Log'],bins=10)
plt.title('Log Transfromed Distance')
plt.show()
