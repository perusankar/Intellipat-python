import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


roll_no = [1,2,3,4,5]
marks = [10,15,25,40,80]

plt.scatter(roll_no,marks,color='red',marker='*',label='Marks')
plt.title("Sales detail")
plt.xlabel("roll")
plt.ylabel("marks")
plt.grid(True)
plt.legend()
plt.show()


category = ["Children 0-18","Adult 19-25","Adult 26-50","Adult 51-70","Senior Citizens"]
values=  [20,30,10,40,10]
plt.pie(values,labels=category,autopct="%0.1f%%")   #autopct is used to show in how much
plt.show()                                           #percentage your data is divideds