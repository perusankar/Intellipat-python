import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mpld3

df = pd.read_csv("cars.csv",skipinitialspace=True)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df.fillna(0, inplace=True)


#sns.pairplot(df,hue='brand')

#plt.show()

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True),annot=True)

plt.show()

print(df['brand'].value_counts())
xx =df['brand'].value_counts()
xx.plot.pie()
plt.show()