import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.DataFrame(
    {
        'x':[1,2,3,4],
        'y':[3,6,7,8]
    }
)
data1=pd.DataFrame(
    {
        'x1':[4,6,8,9],
        'y1':[2,6,8,9]
    }
)
sns.barplot(data=data,x='x',y='y')
sns.barplot(data=data1,x='x1',y='y1')

plt.title("bar example")
plt.show()

