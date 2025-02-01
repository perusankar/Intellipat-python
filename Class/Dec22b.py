import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("cars.csv",skipinitialspace=True)

fig = plt.subplots(2,2, figsize=(15,15))

plt.subplot(2,2,1)
sns.scatterplot(x=df['mpg'],y=df['hp'],hue=df['brand'])
plt.xlabel('Miles Per Gallon')
plt.ylabel('Horse Power')
plt.title('MPG V/S HP')

plt.subplot(2,2,2)
sns.scatterplot(x=df['mpg'],y=df['weightlbs'],hue=df['brand'])
plt.xlabel('Miles Per Gallon')
plt.ylabel('Weight LBS')
plt.title('MPG V/S Weight')

plt.subplot(2,2,3)
sns.scatterplot(x=df['hp'],y=df['mpg'],hue=df['brand'])
plt.xlabel('Horse Power')
plt.ylabel('Miles Per Gallon')
plt.title('MPG V/S HP')

plt.subplot(2,2,4)
sns.scatterplot(x=df['hp'],y=df['time-to-60'],hue=df['brand'])
plt.xlabel('Horse Power')
plt.ylabel('Time to 60')
plt.title('HP V/S Time to 60')

plt.show()