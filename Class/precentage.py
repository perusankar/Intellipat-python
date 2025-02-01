import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mpld3

age = [18,25,30,45,-190,33,67,78,89,93,250,76,99,271,10,13,96,56,35,7,87,97,46,45,78]

Q1 = np.percentile(age,25)
Q2 = np.percentile(age,75)
IQR = Q2 - Q1
print("Q1 " + str(Q1))
print("Q3 " + str(Q2))
print("IDR " + str(IQR))

upperfence = Q2 + 1.5 * IQR
print(upperfence)
lowerfence = Q1 - 1.5 * IQR
print(lowerfence)

for i in age:
    if i > upperfence or i < lowerfence:
        print("outlier " +str(i))
        age.remove(i)

plt.boxplot(age)
plt.show()