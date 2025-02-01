import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("cars.csv")

print("\nFirst 5 rows")
print(df.head(5))
print("\nSize or Shape")
print(df.shape)
print("\nInfo")
df.info()
print("\nDuplicate columns")
null_values = df.duplicated().sum()
print(null_values)