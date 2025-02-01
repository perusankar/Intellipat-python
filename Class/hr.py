import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mpld3

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv(r'HR_DataSet.csv')

df.info()
print(df.isnull().sum())
print(df.head())

print(df['left'].value_counts())
filtered_df = df[df['left'] == 1]
deps = df['Department'].unique()
print("-------------------------------------------------------------------------------")
print(df.describe())
print("-------------------------------------------------------------------------------")

sns.countplot(data=df,x='Department',hue='number_project')
#sns.histplot(data=df,x='average_montly_hours',hue='left')
plt.show()