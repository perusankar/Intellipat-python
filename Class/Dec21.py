import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


x = [1,2,3]
y = [3,2,1]

plt.plot(x,y,color='green',marker='*',label='DDD')
plt.title("Line plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()

days = ["Monday","Tuesday","Wednesday"]
sales = [456,789,340]

plt.bar(days,sales,color=['orange','yellow','blue'])
plt.title("Sales detail")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

roll_no = [1,2,3,4,5]
marks = [10,15,25,40,80]

plt.scatter(roll_no,marks)
plt.title("Sales detail")
plt.xlabel("roll")
plt.ylabel("marks")
plt.grid(True)
plt.show()