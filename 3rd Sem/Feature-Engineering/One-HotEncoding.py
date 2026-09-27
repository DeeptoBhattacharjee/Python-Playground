import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv("Distance.csv")
df2=df.copy()
df2=pd.get_dummies(df2,columns=['Category','Gender'],dtype=int)
print(df2)