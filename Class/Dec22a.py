import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("cars.csv",skipinitialspace=True)

plt.subplot(1,2,1)
sns.scatterplot(x=df['mpg'],y=df['hp'],hue=df['brand'])
plt.title("Cars detail - mhp based on hp")
plt.xlabel("mpg")
plt.ylabel("hp")

plt.subplot(1,2,2)
sns.scatterplot(x=df['mpg'],y=df['weightlbs'],hue=df['brand'])
plt.xlabel('Miles Per Gallon')
plt.ylabel('Weight LBS')
plt.title('MPG V/S Weight')
plt.show()