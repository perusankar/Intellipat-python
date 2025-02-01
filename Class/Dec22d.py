import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mpld3

df = pd.read_csv("cars.csv",skipinitialspace=True)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df.fillna(0, inplace=True)

plt.subplot(2,1,1)
sns.boxplot(x=df['cylinders'],y=df['mpg'],hue=df['brand'])
plt.xlabel('Cylinders')
plt.ylabel('Miles Per Gallon')
plt.title('Cylinders V/S MPG')

plt.subplot(2,1,2)
sns.boxplot(x=df['cylinders'],y=df['weightlbs'],hue=df['brand'])
plt.xlabel('Cylinders')
plt.ylabel('Weight LBS')
plt.title('Cylinders V/S Weight')
#plt.yticks(np.arange(100,5000, step=50))

#plt.show()
mpld3.show()
